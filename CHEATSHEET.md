# ⚡ CHEATSHEET - "Lupa na Prompt"

**Szybka ściągawka komend i najważniejszych informacji**

---

## 🚀 Quick Start (3 komendy)

```bash
# 1. Setup
uv sync

# 2. Analiza (używając istniejących danych)
jupyter notebook analysis_patterns.ipynb
# → Run All Cells

# 3. Wyniki
python quick_summary.py
```

---

## 📊 Kluczowe wyniki (na pamięć)

| Strategia | Accuracy | Zmiana |
|-----------|----------|--------|
| **Prompt (baseline)** | 65.0% | 0.0pp ✅ |
| Uncertainty | 61.7% | -3.3pp |
| Negative Framing | 60.0% | -5.0pp |
| Scepticism | 58.3% | -6.7pp |
| Chain-of-Thought | 57.6% | -7.4pp |
| Positive Framing | 56.7% | -8.3pp |
| Role-Playing (Dummy) | 56.7% | -8.3pp |
| Incentive | 55.8% | -9.2pp |
| Role-Playing (Expert) | 53.3% | -11.7pp ⚠️ |
| **Scrambled_prompt** | 46.9% | -14.0pp ❌ |

**Baseline = Best!** 🏆

---

## 🧠 TOP 5 Wniosków

1. **"Less is More"** - Proste prompty > złożone strategie dla Gemma 3.4B
2. **Scramble = katastrofa** - Błędy ortograficzne: -14.0pp
3. **Expert Role paradoks** - Rola eksperta pogarsza wyniki (-11.7pp)
4. **75% konfliktów** - Model bardzo niestabilny
5. **Halucynacje** - Wykrywanie przez std dev > 0.5

---

## 📁 Struktura projektu (uproszczona)

```
Lupa-na-prompt/
├── test.ipynb                    # ETAP 1: Zbieranie (48 min)
├── analysis_patterns.ipynb       # ETAP 2: Analiza (2 min)
├── prompts2.csv                  # 60 promptów testowych
├── quick_summary.py              # Szybkie wyniki
├── cleanup_duplicates.py         # Czyszczenie duplikatów
├── README.md                     # Start here
├── FINAL_SUMMARY.md              # Wnioski
├── PREZENTACJA.md                # Jak prezentować
└── saved_responses/              # Wyniki (10 plików)
    ├── raw_responses_*.csv       # Surowe dane (84KB)
    ├── parsed_responses_*.csv    # Parsed (2KB)
    ├── report_*.json             # Raport
    └── ...                       # 7 innych CSV
```

---

## 🔑 Komendy (copy-paste)

### Setup pierwsze uruchomienie:
```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
uv sync

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

### Uruchomienie Jupyter:
```bash
# Aktywuj venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # macOS/Linux

# Start Jupyter
jupyter notebook
```

### Szybkie wyniki:
```bash
python quick_summary.py
# Pokazuje: Best/Worst strategy, TOP 5 zmian, Halucynacje, Ryzyko
```

### Cleanup duplikatów:
```bash
python cleanup_duplicates.py
# Usuwa starsze wersje raportów (zostawia najnowsze)
```

### Google API Key:
```bash
# Windows (PowerShell)
$env:GOOGLE_API_KEY = "AIzaSyC..."

# macOS/Linux
export GOOGLE_API_KEY="AIzaSyC..."
```

---

## 📚 Dokumentacja (gdzie co znaleźć)

| Pytanie | Dokument |
|---------|----------|
| **Jak uruchomić?** | [DEPLOYMENT.md](DEPLOYMENT.md) |
| **Co projekt robi?** | [README.md](README.md) |
| **Jakie wyniki?** | [FINAL_SUMMARY.md](FINAL_SUMMARY.md) |
| **Jak prezentować?** | [PREZENTACJA.md](PREZENTACJA.md) |
| **Lista plików?** | [MANIFEST.md](MANIFEST.md) |
| **Szczegóły techniczne?** | [INSTRUKCJA_PROJEKTУ.md](INSTRUKCJA_PROJEKTУ.md) |
| **Status zadań?** | [TODO.md](TODO.md) |

---

## 🎯 12 Strategii promptowania

1. **Prompt** - baseline (bez zmian)
2. **Negative_prompt** - "Myślę, że zawiera błąd"
3. **Positive_prompt** - "Myślę, że to prawidłowe"
4. **Positive_Extra_role** - "Jesteś ekspertem matematyki"
5. **Negative_Extra_role** - "Jesteś socjologiem (nie znasz matematyki)"
6. **Uncertainty_prompt** - "Odpowiedz tylko jeśli pewny"
7. **Scrambled_prompt** - Pomieszany tekst (błędy ortograficzne)
8. **Chain_of_thoughts** - "Przeanalizuj krok po kroku"
9. **Sceptical_role** - "Bądź sceptyczny"
10. **Random_mistake** - Losowe błędy w tekście
11. **Tipping** - "Daj napiwek $200 za poprawną odpowiedź"
12. **High_stakes** - "To bardzo ważne!"

---

## ⚠️ Troubleshooting (najczęstsze problemy)

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: sklearn` | `pip install scikit-learn` |
| `API RESOURCE_EXHAUSTED` | Rate limit - zmniejsz na 10/min lub czekaj 24h |
| `No such file: parsed_responses` | Uruchom `test.ipynb` (ETAP 1) najpierw |
| Jupyter kernel crashed | Restart kernel, zmniejsz dataset (30 zamiast 60 promptów) |
| `IndentationError` w notebook | Użyj `analysis_patterns.ipynb` (nie testOby/test2) |

---

## 📊 Metryki (na szybko)

- **Dataset:** 60 promptów (30 true, 30 false)
- **Model:** Google Gemma 3.4B
- **API calls:** 720 (60 × 12 strategii)
- **Czas zbierania:** ~48 minut (rate limit 15/min)
- **Baseline accuracy:** 65%
- **Worst accuracy:** 46.9% (Scrambled)
- **Konflikty:** 45/60 (75%)
- **Średnia zmienność:** std dev = 0.35

---

## ✅ Checklist prezentacji (5 min)

- [ ] Otworzyć `analysis_patterns.ipynb`
- [ ] Sprawdzić Cell 8 (interactive explorer)
- [ ] Sprawdzić Cell 9 (heatmapa)
- [ ] Uruchomić `python quick_summary.py`
- [ ] Zapamiętać TOP 5 wniosków (wyżej)

---

## 🎓 Rekomendacje (praktyczne)

**✅ RÓB:**
- Używaj prostych, bezpośrednich promptów
- Dodaj "Uncertainty" jeśli chcesz więcej "nie wiem"

**❌ UNIKAJ:**
- Scramble/Noise (błędy ortograficzne)
- Expert Role (paradoksalnie pogarsza)
- Incentives (nie działają)
- Scepticism (dezorientuje)

**⚠️ W PRODUKCJI:**
- Używaj ensemble voting (3+ strategie)
- Monitor zmienność (std dev threshold)
- Automatyczna detekcja halucynacji

---

## 🔗 Quick Links

- **Google Gemini API:** https://aistudio.google.com/app/apikey
- **Python downloads:** https://www.python.org/downloads/
- **UV package manager:** https://astral.sh/uv/
- **Jupyter docs:** https://jupyter.org/

---

## 📞 Support

1. **Błąd w kodzie?** → Sprawdź `README.md` Troubleshooting
2. **Pytanie o wyniki?** → Zobacz `FINAL_SUMMARY.md`
3. **Jak uruchomić?** → Zobacz `DEPLOYMENT.md`
4. **Jak prezentować?** → Zobacz `PREZENTACJA.md`

---

**Powodzenia!** 🚀

*Ostatnia aktualizacja: 2025-12-30*
