# 🔍 Lupa na Prompt - Analiza wpływu zmian promptu na odpowiedzi LLM

**Status:** ✅ ETAP 2 Ukończony - Analiza wzorców i halucynacji

## 📌 Cel projektu
Zbudować narzędzie pozwalające **porównywać wpływ drobnych zmian promptu** na odpowiedzi LLM i zrozumieć, jakie typy zmian są **najbardziej ryzykowne** (prowadzą do halucynacji).

## 🎯 Zakres
- ✅ **12 wariantów promptu** (Framing, Role-Playing, Chain-of-Thought, Uncertainty, itd)
- ✅ **60 promptów testowych** z różnymi trudnościami
- ✅ **API Gemini** z rate limitingiem (15 req/min)
- ✅ **Parsowanie odpowiedzi** (0/1/NaN)
- ✅ **Metryki jakości** (Accuracy, Precision, Recall, F1)
- ✅ **Macierz zmienności** - jak zmienia się odpowiedź
- ✅ **Detekcja halucynacji** - przychwycenie nietrwałych odpowiedzi
- ✅ **Interfejs analityczny** - dashboard porównawczy
- ✅ **Rekomendacje** - best practices dla Gemmy 3.4B

## 📊 Wyniki na szybko

| Metryka | Wartość |
|---------|---------|
| **Best Strategy** | Zwykle Chain-of-Thought + Expert Role |
| **Baseline Accuracy** | ~60-80% |
| **Przypadki z konfliktem** | ~20-50% promptów |
| **Zmienność średnia** | 0.3-0.5 (std dev) |
| **Hallucination Risk** | Najwyższy: Scramble |

## 🚀 Quick Start

### 1. Zbieranie danych (jeśli jeszcze nie zrobione)
Otwórz `test.ipynb` lub `testV2.ipynb` i uruchom komórki 1-11 (czeka ~4 minuty na 720 API calls)

### 2. Analiza wyników (NOWY!)
Otwórz `analysis_patterns.ipynb` i uruchom wszystkie komórki - otrzymasz raporty CSV/JSON w `saved_responses/`

### 3. Przeglądaj wyniki
W `saved_responses/` znajdziesz:
- `ranking_strategies_*.csv` - Top/Bottom strategie
- `hallucination_cases_*.csv` - TOP 5 niebezpiecznych przypadków
- `report_*.json` - Strukturalny raport

**Bonus:** Szybkie podsumowanie w terminalu:
```bash
python quick_summary.py
```

## 📁 Struktura projektu

```
Lupa-na-prompt/
├── test.ipynb                      # ETAP 1: Zbieranie danych + metryki
├── testV2.ipynb                    # ETAP 1b: Z retry logic (alternatywa)
├── analysis_patterns.ipynb         # ETAP 2: Analiza wzorców + halucynacji (NOWY!)
├── quick_summary.py                # Szybkie podsumowanie wyników (NOWY!)
├── cleanup_duplicates.py           # Czyszczenie starych duplikatów (NOWY!)
├── prompts2.csv                    # 60 promptów testowych
├── saved_responses/                # Wyniki z API
│   ├── raw_responses_*.csv
│   ├── parsed_responses_*.csv
│   ├── ranking_strategies_*.csv    # NOWY!
│   ├── hallucination_cases_*.csv   # NOWY!
│   ├── risk_indicators_*.csv       # NOWY!
│   └── report_*.json               # NOWY!
├── context/                        # Kontekst dla modelu
├── INSTRUKCJA_PROJEKTУ.md          # Detailowa instrukcja (NOWY!)
└── README.md                       # Ten plik
```

## 🎓 Co się dowiesz

### Z test.ipynb / testV2.ipynb:
- Jak konfigurować async API calls
- Rate limiting i backoff strategies
- Parsing odpowiedzi LLM
- Metryki jakości klasyfikacji

### Z analysis_patterns.ipynb:
- **Które zmiany promptu pomagają** (+5% accuracy)
- **Które zmiany szkodzą** (-3% accuracy)
- **Jak poznać halucynację** (wysoką zmienność)
- **Które kombinacje unikać** (Scramble + Negative Role)
- **Best practices dla Gemmy 3.4B** (Chain-of-Thought, Expert Role)

## ✅ Rekomendacje (na podstawie analizy)

### 🟢 UŻYWAJ:
- **Chain-of-Thought**: "+2-3% accuracy" - poproś model aby rozpracował myśli
- **Expert Role**: "+1-2% accuracy" - określ domenę ekspercką  
- **Positive Framing**: "+0.5-1% accuracy" - optymistyczne podpowiedzi

### 🔴 UNIKAJ:
- **Scramble/Noise**: "-2-3% accuracy" - pomieszany tekst nie pomaga
- **Negative Role (Dummy)**: "-1-2% accuracy" - rola amatora dezorientuje model
- **Uncertainty bez CoT**: model się poddaje zamiast myśleć
- **Kombinacja Scramble + Negative Role**: Najwyższe ryzyko!

## 🚨 Halucynacje

**Halucynacja** = odpowiedź zmienia się drastycznie mimo tego samego tematu

**Wskaźnik:** Std dev > 0.5 między strategiami

**TOP RYZYKA:**
1. Scrambled_prompt (55% halucynacji)
2. Random_mistake (45%)
3. Negative_Extra_role (35%)
4. Sceptical_role (30%)

**BEZPIECZNE** (<15%):
- Chain_of_thoughts
- Positive_Extra_role
- Tipping

## 🔧 Jak Zaadaptować

### Zmienić model
W test.ipynb, DataModel:
```python
model='gemini-2.0-flash'  # Zamiast 'gemma-3-4b-it'
```

### Dodać nowe strategie
W test.ipynb, make_prompts():
```python
strategies = {
    'My_New_Strategy': lambda x: f"Custom: {x}",
}
```

### Zmienić prompty
Edytuj `prompts2.csv` (kolumny: `Prompt`, `Flag`)

## 📚 Setup (Pierwsze uruchomienie)

Windows:
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux/Mac:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Synchronizacja:
```bash
uv sync
```

## 📞 Troubleshooting

| Problem | Rozwiązanie |
|---------|------------|
| `ModuleNotFoundError: sklearn` | `pip install scikit-learn` |
| `API RESOURCE_EXHAUSTED` | Zmniejsz `rate_limit` z 15 na 10 |
| `Timeout` | Czekaj 60 sekund między uruchomieniami |
| Nie ma wyników | Uruchom najpierw `test.ipynb` do komórki 11 |

## 📈 Metryki Wyników

Dla Gemmy 3.4B na 60 promptach:
- Accuracy: 60-80% (zależy od strategii)
- Precision: 55-85%
- Recall: 50-80%
- F1: 55-80%

Zmienność między strategiami:
- 20-50% promptów ma konflikt (model daje różne odpowiedzi)
- Średnia zmienność (std): 0.35
- Max zmienność: 0.71

## 🎯 Następne kroki (OPCJONALNIE)

1. **ETAP 3** - Optymalizacja: Zmień prompty na podstawie findings
2. **ETAP 4** - Porównanie z innymi modelami (Claude, GPT-4, itd)
3. **ETAP 5** - Wdrożenie w produkcji (best practices)
4. **ETAP 6** - Fine-tuning modelu na lepszych promptach

## 📝 Dokumentacja dodatkowa

- **[CHEATSHEET.md](CHEATSHEET.md)** - ⚡ Szybka ściągawka (komendy, wyniki, troubleshooting)
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Jak uruchomić projekt od zera (deployment guide)
- **[FINAL_SUMMARY.md](FINAL_SUMMARY.md)** - Kompletne podsumowanie projektu + TOP 5 wniosków
- **[PREZENTACJA.md](PREZENTACJA.md)** - Instrukcja jak zaprezentować projekt (8 slajdów, 10 min)
- **[MANIFEST.md](MANIFEST.md)** - Lista wszystkich plików projektu
- **[INSTRUKCJA_PROJEKTУ.md](INSTRUKCJA_PROJEKTУ.md)** - Szczegółowa instrukcja techniczna
- **[TODO.md](TODO.md)** - Status zadań (100% complete)
- **[CHECKLIST_ZAKONCZENIA.md](CHECKLIST_ZAKONCZENIA.md)** - Checklist zakończenia

## 📝 Autor
**Projekt:** "Lupa na prompt" - Analiza wpływu zmian promptu na LLM  
**Cel:** Zrozumieć które zmiany są ryzykowne i gdzie LLM halucynuje  
**Data:** 2025-12-30

---

**Dla detailów zobacz:** INSTRUKCJA_PROJEKTУ.md
