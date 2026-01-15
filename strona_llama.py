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

st.set_page_config(page_title="Lupa na prompt - Analiza LLaMA", layout="wide")
st.title("Lupa na prompt - Analiza wyników LLaMA")

# ============= STYLE =============
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 100)

# ============= WCZYTANIE DANYCH =============
@st.cache_data
def load_data():
    try:
        parsed_df = pd.read_csv("saved_responses_llama/parsed_responses.csv", index_col=0)
        raw_df = pd.read_csv("saved_responses_llama/raw_responses.csv", index_col=0)

        df = pd.read_csv('saved_responses_llama/prompts_made.csv', index_col=0)
        return parsed_df, raw_df, df
    except FileNotFoundError:
        st.error("Brak plików wyników. Uruchom najpierw llama_generation.ipynb")
        st.stop()

parsed_df, raw_df, df = load_data()
y_true = parsed_df['Flag'].values

# ============= METRYKI =============
@st.cache_data
def calculate_metrics():
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

metrics_df = calculate_metrics()

# ============= ZMIENNOŚĆ =============
@st.cache_data
def calculate_variability():
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

var_df = calculate_variability()

# ============= PORÓWNANIE Z PROMPT =============
@st.cache_data
def calculate_comparison():
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

comparison_df = calculate_comparison()

# ============= HALUCYNACJE =============
@st.cache_data
def calculate_hallucinations():
    hallucination_threshold = var_df['Std'].quantile(0.75)
    
    var_df_copy = var_df.copy()
    var_df_copy['Hallucination_Risk'] = var_df_copy['Std'] > hallucination_threshold
    
    high_risk = var_df_copy[var_df_copy['Hallucination_Risk']].sort_values('Std', ascending=False)
    
    return high_risk, hallucination_threshold

high_risk, hallucination_threshold = calculate_hallucinations()

# ============= KATEGORIE STRATEGII =============
@st.cache_data
def calculate_categories():
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

cat_perf_df = calculate_categories()

# ============= GŁÓWNY DASHBOARD =============
col1, col2, col3, col4 = st.columns(4)

with col1:
    best_strat = metrics_df.iloc[0]
    st.metric("Najlepsza strategia", best_strat['Strategy'], f"{best_strat['Accuracy']:.1%}")

with col2:
    baseline_acc = metrics_df[metrics_df['Strategy'] == 'Prompt']['Accuracy'].values[0]
    st.metric("Baseline (Prompt)", f"{baseline_acc:.1%}", f"{(best_strat['Accuracy']-baseline_acc)*100:.1f} pp")

with col3:
    st.metric("Wysokie ryzyko", len(high_risk), f"{len(high_risk)/len(var_df)*100:.1f}%")

with col4:
    conflicts = var_df['Has_Conflict'].sum()
    st.metric("Konflikty", conflicts, f"{conflicts/len(var_df)*100:.1f}%")

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
    st.dataframe(metrics_df[['Strategy', 'Accuracy', 'Precision', 'Recall', 'F1']], use_container_width=True, hide_index=True)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    # Heatmapa poprawności
    strategies_list = [c for c in parsed_df.columns if c != 'Flag' and 'Unnamed' not in c]
    correctness_matrix = np.zeros((len(strategies_list), len(parsed_df)))
    for i, strategy in enumerate(strategies_list):
        for j in range(len(parsed_df)):
            pred = parsed_df[strategy].iloc[j]
            if np.isnan(pred):
                correctness_matrix[i][j] = -1
            else:
                correctness_matrix[i][j] = 1 if pred == y_true[j] else 0
    
    im1 = ax1.imshow(correctness_matrix, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)
    ax1.set_xlabel('Prompt Index')
    ax1.set_ylabel('Strategy')
    ax1.set_yticks(range(len(strategies_list)))
    ax1.set_yticklabels(strategies_list, fontsize=8)
    ax1.set_title('Heatmapa poprawności')
    plt.colorbar(im1, ax=ax1, label='Correctness')
    
    # Ranking
    strategies = metrics_df['Strategy'].values
    accuracies = metrics_df['Accuracy'].values
    colors = plt.cm.viridis(np.linspace(0, 1, len(strategies)))
    
    ax2.barh(strategies, accuracies, color=colors)
    ax2.set_xlabel('Accuracy')
    ax2.set_title('Ranking strategii')
    ax2.set_xlim(0, 1)
    for i, (s, acc) in enumerate(zip(strategies, accuracies)):
        ax2.text(acc + 0.01, i, f'{acc:.1%}', va='center', fontsize=8)
    
    plt.tight_layout()
    st.pyplot(fig)

# --------- TAB 2: PORÓWNANIE ---------
with tab2:
    st.subheader("Zmiana odpowiedzi w porównaniu do Prompt")
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = plt.cm.RdYlGn(comparison_df['Zgodność_z_Prompt_%'] / 100)
    ax.barh(comparison_df['Strategy'], comparison_df['Różnica_od_Prompt_%'], color=colors)
    ax.set_xlabel('% zmian w stosunku do Prompt')
    ax.set_title('Zmienność strategii - porównanie z Prompt (baseline)')
    ax.grid(axis='x', alpha=0.3)
    
    for i, (s, diff, agr) in enumerate(zip(comparison_df['Strategy'], 
                                            comparison_df['Różnica_od_Prompt_%'],
                                            comparison_df['Zgodność_z_Prompt_%'])):
        ax.text(diff + 0.5, i, f'{diff:.1f}% (∑{agr:.0f}%)', va='center', fontsize=9)
    
    plt.tight_layout()
    st.pyplot(fig)

# --------- TAB 3: WZORCE ---------
with tab3:
    st.subheader("Analiza kategorii strategii")
    st.dataframe(cat_perf_df[['Category', 'Avg_Accuracy', 'Impact']], use_container_width=True, hide_index=True)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    # Wpływ kategorii
    colors = ['green' if x > 0 else 'red' for x in cat_perf_df['Impact']]
    ax1.barh(cat_perf_df['Category'], cat_perf_df['Impact'], color=colors, alpha=0.7)
    ax1.axvline(0, color='black', linestyle='-', linewidth=1)
    ax1.set_xlabel('Impact vs Baseline')
    ax1.set_title('Wpływ kategorii na accuracy')
    ax1.grid(axis='x', alpha=0.3)
    
    for i, (cat, imp) in enumerate(zip(cat_perf_df['Category'], cat_perf_df['Impact'])):
        ax1.text(imp + (0.01 if imp > 0 else -0.01), i, f'{imp:+.1%}', 
                ha='left' if imp > 0 else 'right', va='center')
    
    # Trudność vs Zmienność
    baseline_per_prompt = []
    for idx in range(len(parsed_df)):
        row = parsed_df.iloc[idx].dropna()
        if len(row) > 0:
            correct = (row == y_true[idx]).sum()
            pct = correct / len(row)
            baseline_per_prompt.append(pct)
        else:
            baseline_per_prompt.append(0)
    
    baseline_per_prompt = np.array(baseline_per_prompt)
    prompt_difficulty = 1 - baseline_per_prompt
    
    ax2.scatter(prompt_difficulty, var_df.sort_values('Idx')['Std'].values, alpha=0.6, s=100)
    z = np.polyfit(prompt_difficulty, var_df.sort_values('Idx')['Std'].values, 1)
    p = np.poly1d(z)
    ax2.plot(prompt_difficulty, p(prompt_difficulty), "r--", alpha=0.8, linewidth=2)
    ax2.set_xlabel('Trudność')
    ax2.set_ylabel('Zmienność (std)')
    ax2.set_title('Trudne prompty → wyższa zmienność?')
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)

# --------- TAB 4: HALUCYNACJE ---------
with tab4:
    st.subheader("Detekcja halucynacji i ryzyka")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Próg halucynacji:** {hallucination_threshold:.3f}")
        st.write(f"**Przypadki wysokiego ryzyka:** {len(high_risk)}/{len(var_df)} ({len(high_risk)/len(var_df)*100:.1f}%)")
    with col2:
        st.write(f"**Średnia zmienność:** {var_df['Std'].mean():.3f}")
        st.write(f"**Konflikty:** {var_df['Has_Conflict'].sum()}/{len(var_df)} ({var_df['Has_Conflict'].sum()/len(var_df)*100:.1f}%)")
    
    st.subheader("Top 10 przypadków wysokiego ryzyka")
    st.dataframe(high_risk.head(10)[['Idx', 'True', 'Unique_Preds', 'Std']], use_container_width=True, hide_index=True)
    
    # Ryzyko per strategia
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
    
    risk_df = pd.DataFrame(risk_matrix).sort_values('Hallucination_Risk', ascending=False)
    st.dataframe(risk_df, use_container_width=True, hide_index=True)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    colors_risk = plt.cm.RdYlGn_r(risk_df['Hallucination_Risk'] / risk_df['Hallucination_Risk'].max())
    ax1.barh(risk_df['Strategy'], risk_df['Hallucination_Risk'], color=colors_risk)
    ax1.set_xlabel('Risk Score')
    ax1.set_title('Ryzyko halucynacji per strategia')
    ax1.set_xlim(0, 1)
    
    for i, (s, risk) in enumerate(zip(risk_df['Strategy'], risk_df['Hallucination_Risk'])):
        ax1.text(risk + 0.02, i, f'{risk:.1%}', va='center', fontsize=8)
    
    ax2.scatter(risk_df['Hallucination_Risk'], risk_df['Base_Accuracy'], s=200, alpha=0.6)
    for idx, row in risk_df.iterrows():
        ax2.annotate(row['Strategy'], 
                    (row['Hallucination_Risk'], row['Base_Accuracy']),
                    fontsize=8, alpha=0.7)
    
    ax2.set_xlabel('Hallucination Risk')
    ax2.set_ylabel('Accuracy')
    ax2.set_title('Trade-off: Ryzyko vs Dokładność')
    ax2.grid(alpha=0.3)
    ax2.axhline(risk_df['Base_Accuracy'].mean(), color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(risk_df['Hallucination_Risk'].mean(), color='gray', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    st.pyplot(fig)

# --------- TAB 5: CASE STUDY ---------
with tab5:
    st.subheader("Case Study - Analiza pojedynczych promptów")
    
    # Get available strategies (exclude Flag and Unnamed)
    available_strategies = [c for c in parsed_df.columns if c != 'Flag' and 'Unnamed' not in c]
    
    # Strategy selection
    selected_strategies = st.multiselect(
        "Wybierz strategie do wyświetlenia",
        options=available_strategies,
        default=available_strategies[:3] if len(available_strategies) >= 3 else available_strategies
    )
    
    # Initialize session state for case study index
    if 'case_study_idx' not in st.session_state:
        st.session_state.case_study_idx = 0
    
    # Index input
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_idx = st.number_input(
            "Numer indexu promptu (0-{})".format(len(df) - 1),
            min_value=0,
            max_value=len(df) - 1,
            value=st.session_state.case_study_idx,
            step=1
        )
        st.session_state.case_study_idx = selected_idx
    
    # Top 10 variance cases as buttons
    st.write("**Sugestie - Top 10 przypadków o największej zmienności:**")
    top_10_variance = var_df.head(10)
    
    # Create 2 rows of 5 buttons
    for row_num in range(2):
        cols = st.columns(5)
        for col_num in range(5):
            btn_idx = row_num * 5 + col_num
            if btn_idx < len(top_10_variance):
                case = top_10_variance.iloc[btn_idx]
                with cols[col_num]:
                    if st.button(f"#{int(case['Idx'])} (std={case['Std']:.2f})", key=f"case_{btn_idx}"):
                        st.session_state.case_study_idx = int(case['Idx'])
                        st.rerun()
    
    st.divider()
    
    # Display selected prompt details
    if selected_idx < len(df):
        st.subheader(f"Prompt #{selected_idx}")
        
        # Prompt text and flag
        st.write("**Treść promptu:**")
        st.info(df.iloc[selected_idx]['Prompt'])
        
        flag_value = parsed_df['Flag'].iloc[selected_idx]
        st.write(f"**Flag (prawdziwa wartość):** {int(flag_value)}")
        
        # Statistics for this prompt
        var_row = var_df[var_df['Idx'] == selected_idx]
        if len(var_row) > 0:
            var_row = var_row.iloc[0]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Zmienność (Std)", f"{var_row['Std']:.3f}")
            with col2:
                st.metric("Unikalne predykcje", int(var_row['Unique_Preds']))
            with col3:
                st.metric("Konsensus", var_row['Consensus'])
        
        st.divider()
        
        # Display responses for selected strategies
        if selected_strategies:
            st.subheader("Odpowiedzi strategii")
            
            # Display strategies vertically one under another
            for strategy in selected_strategies:
                # Get parsed and raw responses
                parsed_answer = parsed_df[strategy].iloc[selected_idx]
                
                if strategy in raw_df.columns:
                    raw_answer = raw_df[strategy].iloc[selected_idx]
                else:
                    raw_answer = "Brak danych"
                
                # Get the exact prompt used for this strategy
                if strategy in df.columns:
                    strategy_prompt = df[strategy].iloc[selected_idx]
                else:
                    strategy_prompt = "Brak promptu"
                
                # Determine correctness
                if not np.isnan(parsed_answer):
                    is_correct = (parsed_answer == flag_value)
                    bg_color = "#2d5f2e" if is_correct else "#c82333"
                    border_color = "#1e4620" if is_correct else "#a71d2a"
                    text_color = "#ffffff"
                else:
                    bg_color = "#6c757d"
                    border_color = "#5a6268"
                    text_color = "#ffffff"
                    is_correct = None
                
                # Display strategy response in colored box
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
        st.error("Nieprawidłowy index")

# --------- TAB 6: EXPORT ---------
with tab6:
    st.subheader("Eksport wyników")
    
    if st.button("Eksportuj wszystko"):
        folder = 'results_llama'
        Path(folder).mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        metrics_df.to_csv(f'{folder}/ranking_strategies_{timestamp}.csv', index=False)
        comparison_df.to_csv(f'{folder}/comparison_{timestamp}.csv', index=False)
        high_risk.to_csv(f'{folder}/hallucination_cases_{timestamp}.csv', index=False)
        risk_df.to_csv(f'{folder}/risk_indicators_{timestamp}.csv', index=False)
        var_df.to_csv(f'{folder}/variability_analysis_{timestamp}.csv', index=False)
        cat_perf_df.to_csv(f'{folder}/category_performance_{timestamp}.csv', index=False)
        
        report = {
            'metadata': {
                'timestamp': timestamp,
                'model': 'LLaMA 3.3 70B',
                'dataset_size': len(df),
                'n_strategies': len(parsed_df.columns)
            },
            'summary': {
                'best_strategy': str(metrics_df.iloc[0]['Strategy']),
                'best_accuracy': float(metrics_df.iloc[0]['Accuracy']),
                'baseline_accuracy': float(baseline_acc),
                'cases_with_conflict': int(var_df['Has_Conflict'].sum()),
                'conflict_percentage': float(var_df['Has_Conflict'].sum() / len(var_df) * 100)
            }
        }
        
        with open(f'{folder}/report_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        st.success(f"Wyeksportowano do folderu `{folder}/` z timestamp `{timestamp}`")
    
    st.info("Dostępne pliki będą wyeksportowane do folderu results_llama/")
