import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json
import warnings
from datetime import datetime
from glob import glob
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Lupa na prompt - Analiza", layout="wide")
st.title("Lupa na prompt - Porównanie Gemma vs LLaMA")

# ============= STYLE =============
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 100)

# ============= WCZYTANIE DANYCH =============
@st.cache_data
def load_data():
    try:
        # Gemma data
        gemma_parsed = pd.read_csv("saved_responses/parsed_responses.csv", index_col=0)
        gemma_raw = pd.read_csv("saved_responses/raw_responses.csv", index_col=0)
        gemma_df = pd.read_csv('saved_responses/prompts_made.csv', index_col=0)
        
        # LLaMA data
        llama_parsed = pd.read_csv("saved_responses_llama/parsed_responses.csv", index_col=0)
        llama_raw = pd.read_csv("saved_responses_llama/raw_responses.csv", index_col=0)
        llama_df = pd.read_csv('saved_responses_llama/prompts_made.csv', index_col=0)
        
        return {
            'gemma': {'parsed': gemma_parsed, 'raw': gemma_raw, 'prompts': gemma_df},
            'llama': {'parsed': llama_parsed, 'raw': llama_raw, 'prompts': llama_df}
        }
    except FileNotFoundError as e:
        st.error(f"Brak plików wyników: {e}")
        st.stop()

models_data = load_data()

# ============= METRYKI =============
@st.cache_data
def calculate_metrics(parsed_df, y_true):
    metrics_list = []
    for col in parsed_df.columns:
        if col == 'Flag' or 'Unnamed' in col:
            continue
        y_pred = parsed_df[col].values
        valid_mask = ~np.isnan(y_pred)
        
        if valid_mask.sum() > 0:
            y_true_v = y_true[valid_mask]
            y_pred_v = y_pred[valid_mask]
            
            metrics_list.append({
                'Strategy': col,
                'Accuracy': accuracy_score(y_true_v, y_pred_v),
                'Precision': precision_score(y_true_v, y_pred_v, zero_division=0),
                'Recall': recall_score(y_true_v, y_pred_v, zero_division=0),
                'F1': f1_score(y_true_v, y_pred_v, zero_division=0),
                'Valid': valid_mask.sum(),
                'NaN': (~valid_mask).sum()
            })
    
    return pd.DataFrame(metrics_list).sort_values('Accuracy', ascending=False)

# ============= ZMIENNOŚĆ =============
@st.cache_data
def calculate_variability(parsed_df, y_true, df):
    variability_data = []
    
    for idx in range(len(parsed_df)):
        row = parsed_df.iloc[idx].dropna()
        
        if len(row) > 0:
            unique_preds = row.unique()
            has_conflict = len(unique_preds) > 1
            agreements_with_true = (row == y_true[idx]).sum()
            disagreements_with_true = (row != y_true[idx]).sum()
            
            variability_data.append({
                'Idx': idx,
                'Prompt': df.iloc[idx]['Prompt'],
                'True': int(y_true[idx]),
                'Unique_Preds': len(unique_preds),
                'Has_Conflict': has_conflict,
                'Std': row.std(),
                'Consensus': 'STRONG' if disagreements_with_true == 0 or agreements_with_true == 0 else 'WEAK'
            })
    
    return pd.DataFrame(variability_data).sort_values('Std', ascending=False)

# ============= PORÓWNANIE Z PROMPT =============
@st.cache_data
def calculate_comparison(parsed_df):
    baseline_col = 'Prompt'
    comparison_list = []
    
    if baseline_col in parsed_df.columns:
        for col in parsed_df.columns:
            if col == baseline_col or col == 'Flag' or 'Unnamed' in col:
                continue
            
            mask = (~np.isnan(parsed_df[baseline_col])) & (~np.isnan(parsed_df[col]))
            if mask.sum() > 0:
                changes = (parsed_df[baseline_col][mask] != parsed_df[col][mask]).sum()
                pct = changes / mask.sum() * 100
                agreement = (parsed_df[baseline_col][mask] == parsed_df[col][mask]).sum() / mask.sum() * 100
                
                comparison_list.append({
                    'Strategy': col,
                    'Zgodność_z_Prompt_%': agreement,
                    'Różnica_od_Prompt_%': pct,
                    'Próbek': mask.sum()
                })
    
    return pd.DataFrame(comparison_list).sort_values('Różnica_od_Prompt_%', ascending=False)

# ============= HALUCYNACJE =============
@st.cache_data
def calculate_hallucinations(var_df):
    hallucination_threshold = var_df['Std'].quantile(0.75)
    
    var_df_copy = var_df.copy()
    var_df_copy['Hallucination_Risk'] = var_df_copy['Std'] > hallucination_threshold
    
    high_risk = var_df_copy[var_df_copy['Hallucination_Risk']].sort_values('Std', ascending=False)
    
    return high_risk, hallucination_threshold

# ============= KATEGORIE STRATEGII =============
@st.cache_data
def calculate_categories(metrics_df):
    categories = {
        'Positive Framing': ['Positive_prompt'],
        'Negative Framing': ['Negative_prompt'],
        'Role-Playing (Expert)': ['Positive_Extra_role'],
        'Role-Playing (Dummy)': ['Negative_Extra_role'],
        'Chain-of-Thought': ['Chain_of_thoughts'],
        'Uncertainty': ['Uncertainty_prompt'],
        'Scepticism': ['Sceptical_role'],
        'Incentive': ['Tipping', 'High_stakes'],
        'Scramble/Noise': ['Scrambled_prompt', 'Random_mistake']
    }
    
    category_performance = []
    baseline_acc = metrics_df[metrics_df['Strategy'] == 'Prompt']['Accuracy'].values[0]
    
    for cat_name, cat_strategies in categories.items():
        cat_metrics = metrics_df[metrics_df['Strategy'].isin(cat_strategies)]
        if len(cat_metrics) > 0:
            avg_acc = cat_metrics['Accuracy'].mean()
            impact = avg_acc - baseline_acc
            
            category_performance.append({
                'Category': cat_name,
                'Avg_Accuracy': avg_acc,
                'Baseline': baseline_acc,
                'Impact': impact,
                'N_Strategies': len(cat_strategies)
            })
    
    return pd.DataFrame(category_performance).sort_values('Impact', ascending=False)

# ============= RYZYKO =============
@st.cache_data
def calculate_risk(parsed_df, metrics_df, var_df, hallucination_threshold):
    risk_matrix = []
    for strategy in parsed_df.columns:
        if strategy == 'Flag' or 'Unnamed' in strategy:
            continue
        strategy_volatility = []
        
        for idx in range(len(parsed_df)):
            inter_var = var_df[var_df['Idx'] == idx]['Std'].values
            if len(inter_var) > 0 and inter_var[0] > hallucination_threshold:
                row_preds = parsed_df.iloc[idx].dropna()
                if len(row_preds) > 1:
                    pred = parsed_df[strategy].iloc[idx]
                    if not np.isnan(pred):
                        majority = row_preds.mode().values
                        if len(majority) > 0:
                            agrees = pred == majority[0]
                            strategy_volatility.append(not agrees)
        
        if len(strategy_volatility) > 0:
            risk_score = sum(strategy_volatility) / len(strategy_volatility)
        else:
            risk_score = 0
        
        risk_matrix.append({
            'Strategy': strategy,
            'Hallucination_Risk': risk_score,
            'Base_Accuracy': metrics_df[metrics_df['Strategy'] == strategy]['Accuracy'].values[0]
        })
    
    return pd.DataFrame(risk_matrix).sort_values('Hallucination_Risk', ascending=False)

# Process data for both models
gemma_parsed = models_data['gemma']['parsed']
llama_parsed = models_data['llama']['parsed']

gemma_metrics = calculate_metrics(gemma_parsed, gemma_parsed['Flag'].values)
llama_metrics = calculate_metrics(llama_parsed, llama_parsed['Flag'].values)

gemma_var = calculate_variability(gemma_parsed, gemma_parsed['Flag'].values, models_data['gemma']['prompts'])
llama_var = calculate_variability(llama_parsed, llama_parsed['Flag'].values, models_data['llama']['prompts'])

gemma_comparison = calculate_comparison(gemma_parsed)
llama_comparison = calculate_comparison(llama_parsed)

gemma_cat = calculate_categories(gemma_metrics)
llama_cat = calculate_categories(llama_metrics)

gemma_high_risk, gemma_threshold = calculate_hallucinations(gemma_var)
llama_high_risk, llama_threshold = calculate_hallucinations(llama_var)

gemma_risk = calculate_risk(gemma_parsed, gemma_metrics, gemma_var, gemma_threshold)
llama_risk = calculate_risk(llama_parsed, llama_metrics, llama_var, llama_threshold)

# ============= SEKCJE =============
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Metryki", 
    "Porównanie", 
    "Wzorce", 
    "Halucynacje", 
    "Case Study",
    "Export"
])

# --------- TAB 1: METRYKI ---------
with tab1:
    st.subheader("Ranking strategii")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Gemma 3.4B**")
        st.dataframe(gemma_metrics[['Strategy', 'Accuracy', 'Precision', 'Recall', 'F1']], use_container_width=True, hide_index=True)
    
    with col2:
        st.write("**LLaMA 3.3 70B**")
        st.dataframe(llama_metrics[['Strategy', 'Accuracy', 'Precision', 'Recall', 'F1']], use_container_width=True, hide_index=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Heatmapa poprawności - Gemma**")
        fig_g, ax_g = plt.subplots(figsize=(14, 8))
        
        strategies_list = [c for c in gemma_parsed.columns if c != 'Flag' and 'Unnamed' not in c]
        correctness_matrix = np.zeros((len(strategies_list), len(gemma_parsed)))
        y_true_g = gemma_parsed['Flag'].values
        
        for i, strategy in enumerate(strategies_list):
            for j in range(len(gemma_parsed)):
                pred = gemma_parsed[strategy].iloc[j]
                if np.isnan(pred):
                    correctness_matrix[i][j] = -1
                else:
                    correctness_matrix[i][j] = 1 if pred == y_true_g[j] else 0
        
        im_g = ax_g.imshow(correctness_matrix, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)
        ax_g.set_xlabel('Prompt Index')
        ax_g.set_ylabel('Strategy')
        ax_g.set_yticks(range(len(strategies_list)))
        ax_g.set_yticklabels(strategies_list, fontsize=8)
        ax_g.set_title('Heatmapa poprawności - Gemma')
        plt.colorbar(im_g, ax=ax_g, label='Correctness')
        plt.tight_layout()
        st.pyplot(fig_g)
    
    with col2:
        st.write("**Heatmapa poprawności - LLaMA**")
        fig_l, ax_l = plt.subplots(figsize=(14, 8))
        
        strategies_list = [c for c in llama_parsed.columns if c != 'Flag' and 'Unnamed' not in c]
        correctness_matrix = np.zeros((len(strategies_list), len(llama_parsed)))
        y_true_l = llama_parsed['Flag'].values
        
        for i, strategy in enumerate(strategies_list):
            for j in range(len(llama_parsed)):
                pred = llama_parsed[strategy].iloc[j]
                if np.isnan(pred):
                    correctness_matrix[i][j] = -1
                else:
                    correctness_matrix[i][j] = 1 if pred == y_true_l[j] else 0
        
        im_l = ax_l.imshow(correctness_matrix, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)
        ax_l.set_xlabel('Prompt Index')
        ax_l.set_ylabel('Strategy')
        ax_l.set_yticks(range(len(strategies_list)))
        ax_l.set_yticklabels(strategies_list, fontsize=8)
        ax_l.set_title('Heatmapa poprawności - LLaMA')
        plt.colorbar(im_l, ax=ax_l, label='Correctness')
        plt.tight_layout()
        st.pyplot(fig_l)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Ranking - Gemma**")
        fig_g, ax_g = plt.subplots(figsize=(12, 8))
        strategies = gemma_metrics['Strategy'].values
        accuracies = gemma_metrics['Accuracy'].values
        colors = plt.cm.viridis(np.linspace(0, 1, len(strategies)))
        
        ax_g.barh(strategies, accuracies, color=colors)
        ax_g.set_xlabel('Accuracy')
        ax_g.set_title('Ranking strategii - Gemma')
        ax_g.set_xlim(0, 1)
        for i, (s, acc) in enumerate(zip(strategies, accuracies)):
            ax_g.text(acc + 0.01, i, f'{acc:.1%}', va='center', fontsize=8)
        
        plt.tight_layout()
        st.pyplot(fig_g)
    
    with col2:
        st.write("**Ranking - LLaMA**")
        fig_l, ax_l = plt.subplots(figsize=(12, 8))
        strategies = llama_metrics['Strategy'].values
        accuracies = llama_metrics['Accuracy'].values
        colors = plt.cm.viridis(np.linspace(0, 1, len(strategies)))
        
        ax_l.barh(strategies, accuracies, color=colors)
        ax_l.set_xlabel('Accuracy')
        ax_l.set_title('Ranking strategii - LLaMA')
        ax_l.set_xlim(0, 1)
        for i, (s, acc) in enumerate(zip(strategies, accuracies)):
            ax_l.text(acc + 0.01, i, f'{acc:.1%}', va='center', fontsize=8)
        
        plt.tight_layout()
        st.pyplot(fig_l)

# --------- TAB 2: PORÓWNANIE ---------
with tab2:
    st.subheader("Zmiana odpowiedzi w porównaniu do Prompt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Gemma**")
        st.dataframe(gemma_comparison, use_container_width=True, hide_index=True)
        
        fig_g, ax_g = plt.subplots(figsize=(12, 8))
        colors = plt.cm.RdYlGn(gemma_comparison['Zgodność_z_Prompt_%'] / 100)
        ax_g.barh(gemma_comparison['Strategy'], gemma_comparison['Różnica_od_Prompt_%'], color=colors)
        ax_g.set_xlabel('% zmian w stosunku do Prompt')
        ax_g.set_title('Zmienność strategii - Gemma')
        ax_g.grid(axis='x', alpha=0.3)
        
        for i, (s, diff, agr) in enumerate(zip(gemma_comparison['Strategy'], 
                                                gemma_comparison['Różnica_od_Prompt_%'],
                                                gemma_comparison['Zgodność_z_Prompt_%'])):
            ax_g.text(diff + 0.5, i, f'{diff:.1f}% (∑{agr:.0f}%)', va='center', fontsize=9)
        
        plt.tight_layout()
        st.pyplot(fig_g)
    
    with col2:
        st.write("**LLaMA**")
        st.dataframe(llama_comparison, use_container_width=True, hide_index=True)
        
        fig_l, ax_l = plt.subplots(figsize=(12, 8))
        colors = plt.cm.RdYlGn(llama_comparison['Zgodność_z_Prompt_%'] / 100)
        ax_l.barh(llama_comparison['Strategy'], llama_comparison['Różnica_od_Prompt_%'], color=colors)
        ax_l.set_xlabel('% zmian w stosunku do Prompt')
        ax_l.set_title('Zmienność strategii - LLaMA')
        ax_l.grid(axis='x', alpha=0.3)
        
        for i, (s, diff, agr) in enumerate(zip(llama_comparison['Strategy'], 
                                                llama_comparison['Różnica_od_Prompt_%'],
                                                llama_comparison['Zgodność_z_Prompt_%'])):
            ax_l.text(diff + 0.5, i, f'{diff:.1f}% (∑{agr:.0f}%)', va='center', fontsize=9)
        
        plt.tight_layout()
        st.pyplot(fig_l)

# --------- TAB 3: WZORCE ---------
with tab3:
    st.subheader("Analiza kategorii strategii")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Gemma**")
        st.dataframe(gemma_cat[['Category', 'Avg_Accuracy', 'Impact']], use_container_width=True, hide_index=True)
        
        fig_g, ax_g = plt.subplots(figsize=(12, 6))
        colors = ['green' if x > 0 else 'red' for x in gemma_cat['Impact']]
        ax_g.barh(gemma_cat['Category'], gemma_cat['Impact'], color=colors, alpha=0.7)
        ax_g.axvline(0, color='black', linestyle='-', linewidth=1)
        ax_g.set_xlabel('Impact vs Baseline')
        ax_g.set_title('Wpływ kategorii na accuracy - Gemma')
        ax_g.grid(axis='x', alpha=0.3)
        
        for i, (cat, imp) in enumerate(zip(gemma_cat['Category'], gemma_cat['Impact'])):
            ax_g.text(imp + (0.01 if imp > 0 else -0.01), i, f'{imp:+.1%}', 
                    ha='left' if imp > 0 else 'right', va='center')
        
        plt.tight_layout()
        st.pyplot(fig_g)
    
    with col2:
        st.write("**LLaMA**")
        st.dataframe(llama_cat[['Category', 'Avg_Accuracy', 'Impact']], use_container_width=True, hide_index=True)
        
        fig_l, ax_l = plt.subplots(figsize=(12, 6))
        colors = ['green' if x > 0 else 'red' for x in llama_cat['Impact']]
        ax_l.barh(llama_cat['Category'], llama_cat['Impact'], color=colors, alpha=0.7)
        ax_l.axvline(0, color='black', linestyle='-', linewidth=1)
        ax_l.set_xlabel('Impact vs Baseline')
        ax_l.set_title('Wpływ kategorii na accuracy - LLaMA')
        ax_l.grid(axis='x', alpha=0.3)
        
        for i, (cat, imp) in enumerate(zip(llama_cat['Category'], llama_cat['Impact'])):
            ax_l.text(imp + (0.01 if imp > 0 else -0.01), i, f'{imp:+.1%}', 
                    ha='left' if imp > 0 else 'right', va='center')
        
        plt.tight_layout()
        st.pyplot(fig_l)

# --------- TAB 4: HALUCYNACJE ---------
with tab4:
    st.subheader("Detekcja halucynacji i ryzyka")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Gemma**")
        st.write(f"**Próg halucynacji:** {gemma_threshold:.3f}")
        st.write(f"**Przypadki wysokiego ryzyka:** {len(gemma_high_risk)}/{len(gemma_var)} ({len(gemma_high_risk)/len(gemma_var)*100:.1f}%)")
        st.write(f"**Średnia zmienność:** {gemma_var['Std'].mean():.3f}")
        st.write(f"**Konflikty:** {gemma_var['Has_Conflict'].sum()}/{len(gemma_var)} ({gemma_var['Has_Conflict'].sum()/len(gemma_var)*100:.1f}%)")
        
        st.subheader("Top 10 przypadków wysokiego ryzyka - Gemma")
        st.dataframe(gemma_high_risk.head(10)[['Idx', 'True', 'Unique_Preds', 'Std']], use_container_width=True, hide_index=True)
        
        fig_g, (ax1_g, ax2_g) = plt.subplots(2, 1, figsize=(12, 12))
        
        colors_risk = plt.cm.RdYlGn_r(gemma_risk['Hallucination_Risk'] / gemma_risk['Hallucination_Risk'].max())
        ax1_g.barh(gemma_risk['Strategy'], gemma_risk['Hallucination_Risk'], color=colors_risk)
        ax1_g.set_xlabel('Risk Score')
        ax1_g.set_title('Ryzyko halucynacji per strategia - Gemma')
        ax1_g.set_xlim(0, 1)
        
        for i, (s, risk) in enumerate(zip(gemma_risk['Strategy'], gemma_risk['Hallucination_Risk'])):
            ax1_g.text(risk + 0.02, i, f'{risk:.1%}', va='center', fontsize=8)
        
        ax2_g.scatter(gemma_risk['Hallucination_Risk'], gemma_risk['Base_Accuracy'], s=200, alpha=0.6)
        for idx, row in gemma_risk.iterrows():
            ax2_g.annotate(row['Strategy'], 
                        (row['Hallucination_Risk'], row['Base_Accuracy']),
                        fontsize=8, alpha=0.7)
        
        ax2_g.set_xlabel('Hallucination Risk')
        ax2_g.set_ylabel('Accuracy')
        ax2_g.set_title('Trade-off: Ryzyko vs Dokładność - Gemma')
        ax2_g.grid(alpha=0.3)
        ax2_g.axhline(gemma_risk['Base_Accuracy'].mean(), color='gray', linestyle='--', alpha=0.5)
        ax2_g.axvline(gemma_risk['Hallucination_Risk'].mean(), color='gray', linestyle='--', alpha=0.5)
        
        plt.tight_layout()
        st.pyplot(fig_g)
    
    with col2:
        st.write("**LLaMA**")
        st.write(f"**Próg halucynacji:** {llama_threshold:.3f}")
        st.write(f"**Przypadki wysokiego ryzyka:** {len(llama_high_risk)}/{len(llama_var)} ({len(llama_high_risk)/len(llama_var)*100:.1f}%)")
        st.write(f"**Średnia zmienność:** {llama_var['Std'].mean():.3f}")
        st.write(f"**Konflikty:** {llama_var['Has_Conflict'].sum()}/{len(llama_var)} ({llama_var['Has_Conflict'].sum()/len(llama_var)*100:.1f}%)")
        
        st.subheader("Top 10 przypadków wysokiego ryzyka - LLaMA")
        st.dataframe(llama_high_risk.head(10)[['Idx', 'True', 'Unique_Preds', 'Std']], use_container_width=True, hide_index=True)
        
        fig_l, (ax1_l, ax2_l) = plt.subplots(2, 1, figsize=(12, 12))
        
        colors_risk = plt.cm.RdYlGn_r(llama_risk['Hallucination_Risk'] / llama_risk['Hallucination_Risk'].max())
        ax1_l.barh(llama_risk['Strategy'], llama_risk['Hallucination_Risk'], color=colors_risk)
        ax1_l.set_xlabel('Risk Score')
        ax1_l.set_title('Ryzyko halucynacji per strategia - LLaMA')
        ax1_l.set_xlim(0, 1)
        
        for i, (s, risk) in enumerate(zip(llama_risk['Strategy'], llama_risk['Hallucination_Risk'])):
            ax1_l.text(risk + 0.02, i, f'{risk:.1%}', va='center', fontsize=8)
        
        ax2_l.scatter(llama_risk['Hallucination_Risk'], llama_risk['Base_Accuracy'], s=200, alpha=0.6)
        for idx, row in llama_risk.iterrows():
            ax2_l.annotate(row['Strategy'], 
                        (row['Hallucination_Risk'], row['Base_Accuracy']),
                        fontsize=8, alpha=0.7)
        
        ax2_l.set_xlabel('Hallucination Risk')
        ax2_l.set_ylabel('Accuracy')
        ax2_l.set_title('Trade-off: Ryzyko vs Dokładność - LLaMA')
        ax2_l.grid(alpha=0.3)
        ax2_l.axhline(llama_risk['Base_Accuracy'].mean(), color='gray', linestyle='--', alpha=0.5)
        ax2_l.axvline(llama_risk['Hallucination_Risk'].mean(), color='gray', linestyle='--', alpha=0.5)
        
        plt.tight_layout()
        st.pyplot(fig_l)

# --------- TAB 5: CASE STUDY ---------
with tab5:
    st.subheader("Case Study - Analiza pojedynczych promptów")

    # Shared controls
    if 'case_study_idx' not in st.session_state:
        st.session_state.case_study_idx = 0

    available_strategies_g = [c for c in gemma_parsed.columns if c != 'Flag' and 'Unnamed' not in c]
    available_strategies_l = [c for c in llama_parsed.columns if c != 'Flag' and 'Unnamed' not in c]

    max_idx = max(len(models_data['gemma']['prompts']), len(models_data['llama']['prompts'])) - 1

    st.write("**Ustawienia**")
    control_col = st.container()
    with control_col:
        col_ctrl1, col_ctrl2 = st.columns([3, 2])
        with col_ctrl1:
            selected_idx = st.number_input(
                "Numer indexu promptu (wspólny)",
                min_value=0,
                max_value=max_idx,
                value=st.session_state.case_study_idx,
                step=1,
                key="case_idx"
            )
            st.session_state.case_study_idx = selected_idx
        with col_ctrl2:
            st.caption("Podpowiedzi: Top zmienność")
            top_5_g = gemma_var.head(5)
            top_5_l = llama_var.head(5)
            cols = st.columns(5)
            for i, case in top_5_g.reset_index(drop=True).iterrows():
                if cols[i].button(f"G#{int(case['Idx'])}\n(std {case['Std']:.2f})", key=f"g_top_{i}"):
                    st.session_state.case_study_idx = int(case['Idx'])
                    st.rerun()
            cols = st.columns(5)
            for i, case in top_5_l.reset_index(drop=True).iterrows():
                if cols[i].button(f"L#{int(case['Idx'])}\n(std {case['Std']:.2f})", key=f"l_top_{i}"):
                    st.session_state.case_study_idx = int(case['Idx'])
                    st.rerun()

        st.write("**Strategie**")
        col_strat1, col_strat2 = st.columns(2)
        with col_strat1:
            selected_strategies_g = st.multiselect(
                "Strategie Gemma",
                options=available_strategies_g,
                default=available_strategies_g[:3] if len(available_strategies_g) >= 3 else available_strategies_g,
                key="gemma_strategies"
            )
        with col_strat2:
            selected_strategies_l = st.multiselect(
                "Strategie LLaMA",
                options=available_strategies_l,
                default=available_strategies_l[:3] if len(available_strategies_l) >= 3 else available_strategies_l,
                key="llama_strategies"
            )

    st.divider()

    # Display Gemma and LLaMA side by side
    col1, col2 = st.columns(2)

    # GEMMA DISPLAY
    with col1:
        st.subheader(f"Gemma - Prompt #{selected_idx}")
        if selected_idx < len(models_data['gemma']['prompts']):
            st.write("**Treść promptu:**")
            st.info(models_data['gemma']['prompts'].iloc[selected_idx]['Prompt'])

            flag_value_g = gemma_parsed['Flag'].iloc[selected_idx]
            st.write(f"**Flag (prawdziwa wartość):** {int(flag_value_g)}")

            var_row_g = gemma_var[gemma_var['Idx'] == selected_idx]
            if len(var_row_g) > 0:
                var_row_g = var_row_g.iloc[0]
                col_stat1, col_stat2, col_stat3 = st.columns(3)
                with col_stat1:
                    st.metric("Zmienność (Std)", f"{var_row_g['Std']:.3f}")
                with col_stat2:
                    st.metric("Unikalne predykcje", int(var_row_g['Unique_Preds']))
                with col_stat3:
                    st.metric("Konsensus", var_row_g['Consensus'])

            st.divider()

            if selected_strategies_g:
                st.write("**Odpowiedzi strategii**")
                for strategy in selected_strategies_g:
                    parsed_answer = gemma_parsed[strategy].iloc[selected_idx]

                    if strategy in models_data['gemma']['raw'].columns:
                        raw_answer = models_data['gemma']['raw'][strategy].iloc[selected_idx]
                    else:
                        raw_answer = "Brak danych"

                    if strategy in models_data['gemma']['prompts'].columns:
                        strategy_prompt = models_data['gemma']['prompts'][strategy].iloc[selected_idx]
                    else:
                        strategy_prompt = "Brak promptu"

                    if not np.isnan(parsed_answer):
                        is_correct = (parsed_answer == flag_value_g)
                        bg_color = "#2d5f2e" if is_correct else "#c82333"
                        border_color = "#1e4620" if is_correct else "#a71d2a"
                        text_color = "#ffffff"
                    else:
                        bg_color = "#6c757d"
                        border_color = "#5a6268"
                        text_color = "#ffffff"

                    st.markdown(
                        f"""
                        <div style="
                            background-color: {bg_color};
                            border: 2px solid {border_color};
                            border-radius: 5px;
                            padding: 15px;
                            margin-bottom: 15px;
                            color: {text_color};
                            width: 100%;
                            box-sizing: border-box;
                            overflow: hidden;
                        ">
                            <h4 style="margin-top: 0; margin-bottom: 10px; color: {text_color}; word-break: break-word;">{strategy}</h4>
                            <p style="margin: 5px 0; word-break: break-word;"><strong>Użyty prompt:</strong></p>
                            <p style="font-size: 0.85em; background-color: rgba(0,0,0,0.2); padding: 8px; border-radius: 3px; max-height: 120px; overflow-y: auto; margin: 5px 0; word-break: break-word;">{strategy_prompt}</p>
                            <hr style="border-color: rgba(255,255,255,0.3); margin: 8px 0;">
                            <p style="margin: 5px 0; word-break: break-word;"><strong>Odpowiedź surowa:</strong></p>
                            <p style="font-style: italic; background-color: rgba(0,0,0,0.2); padding: 8px; border-radius: 3px; margin: 5px 0; word-break: break-word;">{raw_answer}</p>
                            <p style="margin: 5px 0; word-break: break-word;"><strong>Sparsowana odpowiedź:</strong> {int(parsed_answer) if not np.isnan(parsed_answer) else 'NaN'}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.warning("Wybierz przynajmniej jedną strategię")
        else:
            st.error("Index poza zakresem dla Gemma")

    # LLAMA DISPLAY
    with col2:
        st.subheader(f"LLaMA - Prompt #{selected_idx}")
        if selected_idx < len(models_data['llama']['prompts']):
            st.write("**Treść promptu:**")
            st.info(models_data['llama']['prompts'].iloc[selected_idx]['Prompt'])

            flag_value_l = llama_parsed['Flag'].iloc[selected_idx]
            st.write(f"**Flag (prawdziwa wartość):** {int(flag_value_l)}")

            var_row_l = llama_var[llama_var['Idx'] == selected_idx]
            if len(var_row_l) > 0:
                var_row_l = var_row_l.iloc[0]
                col_stat1, col_stat2, col_stat3 = st.columns(3)
                with col_stat1:
                    st.metric("Zmienność (Std)", f"{var_row_l['Std']:.3f}")
                with col_stat2:
                    st.metric("Unikalne predykcje", int(var_row_l['Unique_Preds']))
                with col_stat3:
                    st.metric("Konsensus", var_row_l['Consensus'])

            st.divider()

            if selected_strategies_l:
                st.write("**Odpowiedzi strategii**")
                for strategy in selected_strategies_l:
                    parsed_answer = llama_parsed[strategy].iloc[selected_idx]

                    if strategy in models_data['llama']['raw'].columns:
                        raw_answer = models_data['llama']['raw'][strategy].iloc[selected_idx]
                    else:
                        raw_answer = "Brak danych"

                    if strategy in models_data['llama']['prompts'].columns:
                        strategy_prompt = models_data['llama']['prompts'][strategy].iloc[selected_idx]
                    else:
                        strategy_prompt = "Brak promptu"

                    if not np.isnan(parsed_answer):
                        is_correct = (parsed_answer == flag_value_l)
                        bg_color = "#2d5f2e" if is_correct else "#c82333"
                        border_color = "#1e4620" if is_correct else "#a71d2a"
                        text_color = "#ffffff"
                    else:
                        bg_color = "#6c757d"
                        border_color = "#5a6268"
                        text_color = "#ffffff"

                    st.markdown(
                        f"""
                        <div style="
                            background-color: {bg_color};
                            border: 2px solid {border_color};
                            border-radius: 5px;
                            padding: 15px;
                            margin-bottom: 15px;
                            color: {text_color};
                            width: 100%;
                            box-sizing: border-box;
                            overflow: hidden;
                        ">
                            <h4 style="margin-top: 0; margin-bottom: 10px; color: {text_color}; word-break: break-word;">{strategy}</h4>
                            <p style="margin: 5px 0; word-break: break-word;"><strong>Użyty prompt:</strong></p>
                            <p style="font-size: 0.85em; background-color: rgba(0,0,0,0.2); padding: 8px; border-radius: 3px; max-height: 120px; overflow-y: auto; margin: 5px 0; word-break: break-word;">{strategy_prompt}</p>
                            <hr style="border-color: rgba(255,255,255,0.3); margin: 8px 0;">
                            <p style="margin: 5px 0; word-break: break-word;"><strong>Odpowiedź surowa:</strong></p>
                            <p style="font-style: italic; background-color: rgba(0,0,0,0.2); padding: 8px; border-radius: 3px; margin: 5px 0; word-break: break-word;">{raw_answer}</p>
                            <p style="margin: 5px 0; word-break: break-word;"><strong>Sparsowana odpowiedź:</strong> {int(parsed_answer) if not np.isnan(parsed_answer) else 'NaN'}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.warning("Wybierz przynajmniej jedną strategię")
        else:
            st.error("Index poza zakresem dla LLaMA")

# --------- TAB 6: EXPORT ---------
with tab6:
    st.subheader("Eksport wyników")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Gemma**")
        if st.button("Eksportuj Gemma"):
            folder = 'results_gemini'
            Path(folder).mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            gemma_metrics.to_csv(f'{folder}/ranking_strategies_{timestamp}.csv', index=False)
            gemma_comparison.to_csv(f'{folder}/comparison_{timestamp}.csv', index=False)
            gemma_high_risk.to_csv(f'{folder}/hallucination_cases_{timestamp}.csv', index=False)
            gemma_risk.to_csv(f'{folder}/risk_indicators_{timestamp}.csv', index=False)
            gemma_var.to_csv(f'{folder}/variability_analysis_{timestamp}.csv', index=False)
            gemma_cat.to_csv(f'{folder}/category_performance_{timestamp}.csv', index=False)
            
            report = {
                'metadata': {
                    'timestamp': timestamp,
                    'model': 'Gemma 3.4B',
                    'dataset_size': len(models_data['gemma']['prompts']),
                    'n_strategies': len(gemma_parsed.columns)
                },
                'summary': {
                    'best_strategy': str(gemma_metrics.iloc[0]['Strategy']),
                    'best_accuracy': float(gemma_metrics.iloc[0]['Accuracy']),
                    'baseline_accuracy': float(gemma_metrics[gemma_metrics['Strategy'] == 'Prompt']['Accuracy'].values[0]),
                    'cases_with_conflict': int(gemma_var['Has_Conflict'].sum()),
                    'conflict_percentage': float(gemma_var['Has_Conflict'].sum() / len(gemma_var) * 100)
                }
            }
            
            with open(f'{folder}/report_{timestamp}.json', 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            st.success(f"Wyeksportowano Gemma do `{folder}/` z timestamp `{timestamp}`")
    
    with col2:
        st.write("**LLaMA**")
        if st.button("Eksportuj LLaMA"):
            folder = 'results_llama'
            Path(folder).mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            llama_metrics.to_csv(f'{folder}/ranking_strategies_{timestamp}.csv', index=False)
            llama_comparison.to_csv(f'{folder}/comparison_{timestamp}.csv', index=False)
            llama_high_risk.to_csv(f'{folder}/hallucination_cases_{timestamp}.csv', index=False)
            llama_risk.to_csv(f'{folder}/risk_indicators_{timestamp}.csv', index=False)
            llama_var.to_csv(f'{folder}/variability_analysis_{timestamp}.csv', index=False)
            llama_cat.to_csv(f'{folder}/category_performance_{timestamp}.csv', index=False)
            
            report = {
                'metadata': {
                    'timestamp': timestamp,
                    'model': 'LLaMA 3.3 70B',
                    'dataset_size': len(models_data['llama']['prompts']),
                    'n_strategies': len(llama_parsed.columns)
                },
                'summary': {
                    'best_strategy': str(llama_metrics.iloc[0]['Strategy']),
                    'best_accuracy': float(llama_metrics.iloc[0]['Accuracy']),
                    'baseline_accuracy': float(llama_metrics[llama_metrics['Strategy'] == 'Prompt']['Accuracy'].values[0]),
                    'cases_with_conflict': int(llama_var['Has_Conflict'].sum()),
                    'conflict_percentage': float(llama_var['Has_Conflict'].sum() / len(llama_var) * 100)
                }
            }
            
            with open(f'{folder}/report_{timestamp}.json', 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            st.success(f"Wyeksportowano LLaMA do `{folder}/` z timestamp `{timestamp}`")
