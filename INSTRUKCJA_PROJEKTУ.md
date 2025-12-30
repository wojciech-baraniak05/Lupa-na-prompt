# 📚 Instrukcja projektu "Lupa na prompt" - ETAP 2 UKOŃCZONY

## 🎯 Cel projektu
Zbudować narzędzie do **analizy wpływu zmian promptu** na odpowiedzi LLM i zidentyfikować które typy zmian są **najbardziej ryzykowne** (prowadzą do halucynacji).

---

## 📊 Struktura projektu

### ETAP 1: Zbieranie danych (✅ UKOŃCZONY)
**Plik:** `test.ipynb` lub `testV2.ipynb`

**Co robi:**
- Wczytuje 60 promptów z `prompts2.csv`
- Generuje 12 wariantów każdego promptu (różne strategie)
- Wysyła do API Gemmy 3.4B (720 żądań total)
- Z **rate limiting** 15 req/min (4 sekundy na prompt)
- Parsuje odpowiedzi (ekstrahuje 0/1 lub NaN)
- Oblicza metryki (Accuracy, Precision, Recall, F1)
- Zapisuje wyniki do `saved_responses/`

**Strategie promptu:**
1. `Prompt` - baseline (bez zmiany)
2. `Negative_prompt` - "Myślę, że zawiera błąd"
3. `Positive_prompt` - "Myślę, że to prawidłowe"
4. `Positive_Extra_role` - "Jesteś ekspertem"
5. `Negative_Extra_role` - "Jesteś socjologiem"
6. `Uncertainty_prompt` - "Tylko jeśli pewny"
7. `Scrambled_prompt` - "Tekst pomieszany"
8. `Chain_of_thoughts` - "Przeanalizuj krok po kroku"
9. `Sceptical_role` - "Jesteś sceptykiem"
10. `High_stakes` - "Od tego zależy życie"
11. `Tipping` - "Dostaniesz napiwek"
12. `Random_mistake` - "Tekst z błędami"

---

### ETAP 2: Analiza wzorców (✅ UKOŃCZONY - TEN NOTEBOOK)
**Plik:** `analysis_patterns.ipynb`

**Co robi:**

#### 🔹 SEKCJA 1: Przygotowanie danych
- Wczytuje zapisane wyniki z `saved_responses/`
- Oblicza metryki dla każdej strategii
- Tworzy **macierz zmienności** - ile % odpowiedzi się zmienia między strategiami
- Identyfikuje prompty z **konfliktem strategii** (model się nie zgadza sam ze sobą)

#### 🔹 SEKCJA 2: Dashboard analityczny
- Funkcja `display_comparison(idx)` - detailowy przegląd dla wybranego promptu
- Pokazuje: oryginalny prompt → wszystkie warianty → predykcje → poprawność
- Wizualizacja heatmapy poprawności strategii
- Ranking strategii po accuracy

#### 🔹 SEKCJA 3: Analiza wzorców
- Dla każdej **kategorii zmian** (Role, Framing, CoT, itd.) oblicza wpływ na accuracy
- Tworzy mapę: "+Positive_Extra_role = +5.2%", "-Scrambled = -3.1%"
- Korelacja: Trudne prompty → Wyższa zmienność?
- Identyfikuje **"sweet spot"** - co działa najlepiej

#### 🔹 SEKCJA 4: Halucynacje i ryzyko
- **Halucynacja** = odpowiedź zmienia się drastycznie mimo tego samego tematu
- Oblicza **Hallucination Risk Score** dla każdej strategii (0-100%)
- TOP 5 najniebezpieczniejszych przypadków
- Heatmapa: Strategie vs Poziom ryzyka

#### 🔹 SEKCJA 5: Raport końcowy
- Ranking strategii (TOP 3 best, TOP 3 worst)
- Rekomendacje: CO ROBIĆ i CZEGO UNIKAĆ
- "Lessons Learned" - co działa dla Gemmy 3.4B
- **Export wyników** do CSV i JSON

#### 🔹 BONUS: Interaktywny explorer
- 3 konkretne przykłady analizy:
  - Najprostszy prompt
  - Najtrudniejszy prompt
  - Gdzie Chain-of-Thought zmienił wynik

---

## 🚀 Jak uruchomić

### Krok 1: Zbierz dane
```bash
# Uruchom test.ipynb lub testV2.ipynb
# Komórka 1-5: Import + konfiguracja
# Komórka 6-7: Instancja DataModel
# Komórka 8-9: await data_model.prompts() - czeka ~4 minuty
# Komórka 10: data_model.parsowanie() - parsuje odpowiedzi
# Komórka 11: save_results() - zapisuje wyniki
```

### Krok 2: Analizuj wyniki
```bash
# Uruchom analysis_patterns.ipynb
# Komórka 1-2: Importy + wczytanie danych
# Komórka 3-4: Sekcja 1 - Przygotowanie danych
# Komórka 5-6: Sekcja 2 - Dashboard
# Komórka 7-8: Sekcja 3 - Wzorce
# Komórka 9-10: Sekcja 4 - Halucynacje
# Komórka 11-12: Sekcja 5 - Raport + Export
# Komórka 13-15: Bonus - Interaktywne przykłady
```

---

## 📈 Wyniki i Wnioski

### Metryki
- **Best Strategy:** Zależy od danych, zwykle Chain-of-Thought + Expert Role
- **Accuracy:** ~60-80% (zależy od trudności promptów)
- **Zmienność:** 20-50% promptów ma konflikt strategii
- **Hallucination Risk:** Najwyższy dla Scramble + Negative Role

### Rekomendacje
✅ **UŻYWAJ:**
- Chain-of-Thought (rozpracuj myśli)
- Expert Role (określ domenę ekspercką)
- Positive Framing (optymistyczne podpowiedzi)

❌ **UNIKAJ:**
- Scramble/Noise (pomieszany tekst)
- Dummy Role (rola amatora)
- Uncertainty bez CoT (model się poddaje)

---

## 📁 Struktura plików wynikowych

```
saved_responses/
├── raw_responses_*.csv              # Surowe odpowiedzi modelu
├── parsed_responses_*.csv           # Sparsowane (0/1/NaN)
├── ranking_strategies_*.csv         # Ranking accuracy każdej strategii
├── transition_matrix_*.csv          # % zmian między strategiami
├── hallucination_cases_*.csv        # TOP 5 przypadków halucynacji
├── risk_indicators_*.csv            # Risk score per strategia
├── variability_analysis_*.csv       # Std dev zmienności
└── report_*.json                    # Strukturalny report
```

---

## 🔧 Jak dostosować projekt

### Zmienić model
W `test.ipynb`, komórka DataModel:
```python
model='gemma-3-4b-it'  # Zmień na: gemini-2.0-flash, itd
```

### Dodać nowe strategie
W `test.ipynb`, metoda `make_prompts()`:
```python
strategies = {
    'My_Strategy': lambda x: f"Custom prompt: {x}",
    ...
}
```

### Zmienić prompty
Edytuj `prompts2.csv` (kolumna `Prompt` i `Flag`)

### Zmienić progi ryzyka
W `analysis_patterns.ipynb`, sekcja 4:
```python
hallucination_threshold = var_df['Std'].quantile(0.75)  # Zmień z 0.75
```

---

## 🎓 Co się nauczyłeś

1. **Prompt Engineering** - które zmiany wpływają na LLM
2. **Rate Limiting** - jak pracować z API bez przegrzewania
3. **Async/Await** - asynchroniczne żądania do API
4. **Data Analysis** - metryki, zmienność, wzorce
5. **Explainability** - zrozumienie decyzji modelu
6. **Hallucination Detection** - jak poznać gdy model się myli

---

## 📞 Troubleshooting

### Błąd: "Nie znaleziono plików CSV"
→ Uruchom najpierw `test.ipynb` do komórki 11 (save_results)

### Błąd: "ModuleNotFoundError: sklearn"
→ W terminalu: `pip install scikit-learn`

### Błąd: "API RESOURCE_EXHAUSTED"
→ Zmniejsz `rate_limit` z 15 na 10 w DataModel

### Błąd: "Timeout"
→ Poczekaj 60 sekund między uruchomieniami

---

## 📚 Dodatkowe zasoby

- [Google Gemini API Docs](https://ai.google.dev/)
- [Prompt Engineering Best Practices](https://github.com/openai/openai-cookbook)
- [Hallucination in LLMs](https://arxiv.org/abs/2305.13242)

---

**Projekt ukończony:** 2025-12-30
**Status:** ✅ ETAP 2 Ukończony (Analiza wzorców)
**Następny krok:** ETAP 3 - Optymalizacja promptów na podstawie findings (opcjonalnie)
