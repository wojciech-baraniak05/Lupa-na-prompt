# 🎬 INSTRUKCJA PREZENTACJI - "Lupa na Prompt"

**Jak zaprezentować projekt w 5-10 minut**

---

## 🎯 Slajd 1: Tytuł (30 sek)

**"Lupa na Prompt"**  
Analiza wpływu zmian promptu na odpowiedzi LLM Gemma 3.4B

- 60 promptów matematycznych
- 12 strategii promptowania
- 720 wywołań API
- Cel: Zidentyfikować które zmiany pomagają, a które szkodzą

---

## 📊 Slajd 2: Metodologia (1 min)

### Dataset:
- **60 zdań** matematycznych (30 prawdziwych, 30 fałszywych)
- **Model:** Google Gemma 3.4B przez Gemini API
- **12 strategii modyfikacji:**
  - Framing (Positive/Negative)
  - Role-Playing (Expert/Dummy)
  - Chain-of-Thought
  - Uncertainty, Scepticism
  - Incentives (Tipping, High-stakes)
  - Noise (Scramble, Random mistakes)

### Proces:
1. **ETAP 1:** Zbieranie danych (test.ipynb) - 720 API calls
2. **ETAP 2:** Analiza wzorców (analysis_patterns.ipynb) - metryki, halucynacje, risk scoring

---

## 🏆 Slajd 3: Główne wyniki (2 min)

### Baseline = Najlepszy!
- **Prosty prompt bez modyfikacji:** 65% accuracy
- **Best strategy:** Prompt (baseline) 
- **Worst strategy:** Scrambled_prompt (46.9%)

### TOP 5 Najbardziej szkodliwych zmian:
1. **Scramble/Noise:** -14.0pp (błędy ortograficzne totalna katastrofa)
2. **Expert Role:** -11.7pp (paradoks - role eksperta pogarsza wyniki!)
3. **Incentive:** -9.2pp (nagrody nie motywują modelu)
4. **Positive Framing:** -8.3pp
5. **Chain-of-Thought:** -7.4pp

### Kluczowe odkrycie: "Less is More"
- **Dla małych modeli (3.4B) złożone strategie POGARSZAJĄ wyniki**
- Dodatkowe instrukcje przeciążają "kognitywną pojemność" modelu
- **Wniosek:** Gemma 3.4B działa najlepiej z prostymi, bezpośrednimi pytaniami

---

## 🚨 Slajd 4: Halucynacje (2 min)

### Niestabilność modelu:
- **75% promptów** ma konflikty między strategiami (45/60)
- Ta sama treść → różne odpowiedzi w zależności od strategii
- **Średnia zmienność:** std dev = 0.35

### TOP 3 Najbardziej halucynogenne strategie:
1. **Scrambled_prompt:** zmienność 0.71, hallucination risk 89%
2. **Random_mistake:** zmienność 0.65, risk 88%
3. **Sceptical_role:** zmienność 0.55, risk 85%

### Wykrywanie halucynacji:
- **Threshold:** std dev > 0.5 między strategiami
- **Wskaźnik:** Jeśli tylko 1-2 strategie zgadzają się z prawdą → HALUCYNACJA

### Przykład:
*Prompt #0: "Przecięcie dowolnej rodziny sigma-ciał..."*
- Error rate: 45.5%
- Std: 0.522
- Niektóre strategie: 1, inne: 0, chaos!

---

## 📈 Slajd 5: Wizualizacje (1 min)

**POKAŻ NA ŻYWO:**
1. Otwórz `analysis_patterns.ipynb`
2. Scroll do **Cell 8** - interaktywny explorer (ipywidgets slider)
3. Pokaż jak zmienia się odpowiedź dla różnych strategii
4. Scroll do **Cell 9** - heatmapa poprawności strategii
5. Scroll do **Cell 12** - wykres impacts kategorii

**Alternatywnie:**
- Uruchom `python quick_summary.py` w terminalu - pokazuje wszystkie wyniki w 1 sekundę

---

## ✅ Slajd 6: Rekomendacje (1 min)

### Dla użytkowników Gemmy 3.4B:

**✅ RÓB:**
- Używaj prostych, bezpośrednich promptów (baseline)
- Dodaj "Uncertainty" jeśli chcesz więcej "nie wiem" (-3.3pp to OK)

**❌ NIE RÓB:**
- Scramble/Noise (błędy ortograficzne) → -14pp
- Expert Role → -11.7pp
- Incentives (tipping, high-stakes) → -9.2pp
- Scepticism → -6.7pp

### Praktyczne zastosowanie:
- **Produkcja:** Używaj ensemble voting (3+ strategie) + confidence scoring
- **QA:** Automatyczna detekcja halucynacji (std dev threshold)
- **Research:** Porównaj z większymi modelami (GPT-4, Claude) - czy "less is more" dalej działa?

---

## 🎓 Slajd 7: Wnioski naukowe (1 min)

### 1. "Less is More" dla małych modeli
- Modele 3-4B mają ograniczoną "kognitywną pojemność"
- Złożone instrukcje (CoT, role) przeciążają kontekst
- Baseline pozwala modelowi działać intuicyjnie

### 2. Paradoks expertness
- Rola eksperta (-11.7pp) jest GORSZA niż brak roli
- Hipoteza: model interpretuje "jesteś ekspertem" jako presję → "analysis paralysis"

### 3. Ekstremalna niestabilność
- 75% konflikty → Gemma 3.4B nie nadaje się do produkcji bez weryfikacji
- Potrzeba ensemble lub voting mechanizmów
- Single-shot predictions = bardzo ryzykowne

### 4. Noise = katastrofa
- Scramble (-14pp) to największy zabójca accuracy
- Model nie radzi sobie z błędami ortograficznymi
- W przeciwieństwie do ludzi, którzy "autokorekują"

---

## 💡 Slajd 8: Pytania i odpowiedzi

**Spodziewane pytania:**

**Q: Dlaczego Chain-of-Thought pogarsza wyniki?**
A: Dla małych modeli (3.4B) dodatkowe instrukcje przeciążają kontekst. Większe modele (GPT-4) prawdopodobnie skorzystają z CoT.

**Q: Czy baseline=65% to dobry wynik?**
A: Dla matematyki - średnio. Ale ważniejsze że pokazaliśmy WZGLĘDNE różnice między strategiami.

**Q: Jak to użyć w praktyce?**
A: (1) Unikaj Scramble/Expert Role/Incentives dla Gemmy 3.4B, (2) Używaj ensemble voting dla pewności, (3) Monitor zmienność jako wskaźnik halucynacji.

**Q: Co dalej?**
A: ETAP 3 (opcjonalne): Porównanie z GPT-4/Claude, fine-tuning, production deployment.

---

## 📁 Demo Live (jeśli czas pozwala)

### Opcja A: Jupyter Notebook (2 min)
```bash
# Otwórz analysis_patterns.ipynb
# Run all cells (jeśli nie executed)
# Pokaż:
# - Cell 8: Interactive explorer
# - Cell 9: Heatmapa + ranking
# - Cell 16: Risk vs Accuracy scatter plot
```

### Opcja B: Quick Summary Script (30 sek)
```bash
python quick_summary.py
# Pokazuje wszystkie kluczowe wyniki w terminalu
```

### Opcja C: Saved Files (1 min)
```bash
cd saved_responses/
# Pokaż pliki:
# - report_*.json (strukturalny raport)
# - hallucination_cases_*.csv (TOP cases)
# - ranking_strategies_*.csv (best/worst)
```

---

## 🎬 Timeline całości (9-10 min)

| Czas | Slajd | Treść |
|------|-------|-------|
| 0:00-0:30 | 1 | Tytuł + cele |
| 0:30-1:30 | 2 | Metodologia |
| 1:30-3:30 | 3 | Główne wyniki ("Less is More") |
| 3:30-5:30 | 4 | Halucynacje + niestabilność |
| 5:30-6:30 | 5 | Demo wizualizacji |
| 6:30-7:30 | 6 | Rekomendacje |
| 7:30-8:30 | 7 | Wnioski naukowe |
| 8:30-10:00 | 8 | Q&A |

---

## ✅ Checklist przed prezentacją

- [ ] Jupyter notebook `analysis_patterns.ipynb` gotowy (wszystkie cele executed)
- [ ] `quick_summary.py` działa (test: `python quick_summary.py`)
- [ ] Pliki w `saved_responses/` są aktualne
- [ ] Przygotowane slajdy (lub markdown prezentacja)
- [ ] Backup: screenshots z notebooka (jeśli live demo się nie uda)
- [ ] Znasz 5 TOP wniosków na pamięć
- [ ] Przećwiczone odpowiedzi na FAQ

---

## 🎯 Kluczowe punkty do zapamiętania

1. **"Less is More"** - baseline > złożone strategie dla Gemmy 3.4B
2. **Scramble = -14pp** - największa katastrofa
3. **Expert Role = -11.7pp** - paradoks
4. **75% konfliktów** - model bardzo niestabilny
5. **Hallucination detection** - std dev > 0.5

**Powodzenia!** 🚀
