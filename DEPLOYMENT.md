# 🚀 DEPLOYMENT GUIDE - "Lupa na Prompt"

**Jak uruchomić projekt od zera na nowym komputerze**

---

## 📋 Wymagania systemowe

- **OS:** Windows 10/11, macOS, Linux
- **Python:** 3.12+ (zalecane 3.12.7)
- **RAM:** 4GB minimum (8GB+ zalecane dla Jupyter)
- **Disk:** ~500MB (projekt + dependencies)
- **Internet:** Wymagany (API calls do Google Gemini)

---

## 🔧 Krok 1: Klonowanie/Download projektu

### Opcja A: Git clone
```bash
git clone <repository-url>
cd Lupa-na-prompt
```

### Opcja B: Download ZIP
1. Pobierz ZIP z projektu
2. Rozpakuj do wybranego folderu
3. Otwórz terminal w tym folderze

---

## 🐍 Krok 2: Instalacja Python i uv

### Windows:
```powershell
# Sprawdź czy Python 3.12+ zainstalowany
python --version

# Jeśli nie ma - zainstaluj z: https://www.python.org/downloads/

# Instalacja uv (package manager)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS/Linux:
```bash
# Sprawdź Python
python3 --version

# Instalacja uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 📦 Krok 3: Instalacja zależności

```bash
# Synchronizacja projektu (tworzy .venv + instaluje pakiety)
uv sync

# To zainstaluje:
# - pandas, numpy
# - matplotlib, seaborn
# - ipywidgets
# - scikit-learn
# - google-generativeai
# - jupyter
```

**Czas:** ~2-3 minuty

---

## 🔑 Krok 4: Google API Key (WYMAGANE dla ETAP 1)

### A. Uzyskanie API Key:
1. Idź do: https://aistudio.google.com/app/apikey
2. Zaloguj się (Google account)
3. Kliknij "Create API Key"
4. Skopiuj klucz (np. `AIzaSyC...`)

### B. Ustawienie klucza:

**Opcja 1: Environment variable (zalecane)**
```bash
# Windows (PowerShell)
$env:GOOGLE_API_KEY = "AIzaSyC..."

# macOS/Linux
export GOOGLE_API_KEY="AIzaSyC..."
```

**Opcja 2: Hardcode w notebook**
```python
# W test.ipynb, Cell 2:
import os
os.environ['GOOGLE_API_KEY'] = 'AIzaSyC...'  # Twój klucz tutaj
```

⚠️ **UWAGA:** Nie commituj API key do Git!

---

## 📓 Krok 5: Uruchomienie Jupyter

```bash
# Aktywuj virtual environment
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Uruchom Jupyter
jupyter notebook
```

**Alternatywnie:** Otwórz folder w VS Code i uruchom notebooki bezpośrednio.

---

## 🧪 Krok 6: Uruchomienie analizy

### OPCJA A: Użyj istniejących danych (SZYBKO - 2 min)

Jeśli folder `saved_responses/` zawiera pliki:
- `raw_responses_*.csv`
- `parsed_responses_*.csv`

To możesz pominąć ETAP 1 i przejść od razu do:

1. Otwórz `analysis_patterns.ipynb`
2. Run All Cells (Ctrl+Shift+Enter)
3. Czekaj ~1-2 minuty na generowanie wykresów
4. Sprawdź `saved_responses/` - nowe pliki (ranking, hallucination_cases, etc.)

✅ **Gotowe!**

---

### OPCJA B: Zbieraj dane od zera (WOLNO - 48 min)

Jeśli chcesz powtórzyć cały eksperyment:

#### 1. ETAP 1: Zbieranie danych

```bash
# Otwórz test.ipynb w Jupyter
```

**Komórki do wykonania:**
1. Cell 1-2: Importy + setup API key
2. Cell 3: Wczytanie prompts2.csv (60 promptów)
3. Cell 4-5: Definicja DataModel + 12 strategii
4. Cell 6: **UWAGA - długie!** Zbieranie 720 odpowiedzi
   - Rate limit: 15 req/min
   - Czas: ~48 minut
   - Możesz przerwać (Ctrl+C) i wznowić później
5. Cell 7-11: Parsowanie + diagnostyka

**Output:**
- `saved_responses/raw_responses_*.csv` (84KB)
- `saved_responses/parsed_responses_*.csv` (2KB)
- `saved_responses/controversial_*.csv`
- `saved_responses/metrics_*.csv`

#### 2. ETAP 2: Analiza (szybko - 2 min)

```bash
# Otwórz analysis_patterns.ipynb
```

**Run All Cells:**
- Cell 1-19 wykonają się automatycznie
- Wykresy + eksport

**Output:**
- 6 nowych plików CSV/JSON w `saved_responses/`

---

## 🔍 Krok 7: Weryfikacja wyników

### Quick Summary:
```bash
python quick_summary.py
```

**Output:**
```
======================================================================
📊 LUPA NA PROMPT - PODSUMOWANIE WYNIKÓW
======================================================================

🔬 Dataset:
  Model: Gemma 3.4B
  Promptów: 60
  Strategii: 12

🏆 Wyniki:
  Best Strategy: Prompt (65.0%)
  Worst Strategy: Scrambled_prompt (46.9%)
  ...
```

### Sprawdź pliki:
```bash
ls saved_responses/
# Powinno być 10 plików:
# - raw_responses, parsed_responses (ETAP 1)
# - controversial, metrics (ETAP 1)
# - ranking, transition_matrix, hallucination_cases (ETAP 2)
# - risk_indicators, variability_analysis, report.json (ETAP 2)
```

---

## 🐛 Troubleshooting

### Problem 1: `ModuleNotFoundError: No module named 'sklearn'`
**Solution:**
```bash
pip install scikit-learn
```

### Problem 2: `API RESOURCE_EXHAUSTED` (Google API limit)
**Przyczyna:** Za dużo requestów (rate limit 15/min lub 1500/day)

**Solution:**
```python
# W test.ipynb, zmień rate_limit:
self.rate_limit = 10  # Zamiast 15
```
Lub czekaj 24h na reset quota.

### Problem 3: `No such file: saved_responses/parsed_responses_*.csv`
**Przyczyna:** Nie uruchomiłeś test.ipynb (ETAP 1)

**Solution:**
- Albo uruchom test.ipynb do Cell 11
- Albo użyj przykładowych danych (jeśli dostępne)

### Problem 4: Jupyter notebook kernel crashed
**Przyczyna:** Za mało RAM lub zbyt duże dane

**Solution:**
```bash
# Restart kernel i uruchom komórki pojedynczo
# Zmniejsz dataset (użyj tylko 30 promptów zamiast 60)
```

### Problem 5: `IndentationError` w notebook
**Przyczyna:** Uszkodzone komórki

**Solution:**
- Użyj `analysis_patterns.ipynb` (najnowsza wersja - 19 komórek)
- Unikaj testOby.ipynb, test2.ipynb (backup - mogą być błędy)

---

## 🔄 Cleanup i restart

### Usunięcie starych wyników:
```bash
python cleanup_duplicates.py
# Usuwa starsze duplikaty raportów
```

### Restart od zera:
```bash
# Usuń wszystkie wyniki
rm -rf saved_responses/*

# Lub Windows:
Remove-Item saved_responses\* -Force

# Uruchom test.ipynb od początku
```

---

## 📚 Co dalej?

Po pomyślnym uruchomieniu:

1. **Przeczytaj wyniki:**
   - `FINAL_SUMMARY.md` - główne wnioski
   - `saved_responses/report_*.json` - strukturalny raport

2. **Eksperymentuj:**
   - Zmień strategie w `test.ipynb`
   - Dodaj nowe prompty w `prompts2.csv`
   - Przetestuj inny model (np. `gemini-2.0-flash`)

3. **Prezentuj:**
   - Zobacz `PREZENTACJA.md` - instrukcja prezentacji
   - Przygotuj slajdy z wykresami z `analysis_patterns.ipynb`

---

## ✅ Checklist deployment

- [ ] Python 3.12+ zainstalowany
- [ ] `uv sync` wykonany (dependencies)
- [ ] Google API Key ustawiony
- [ ] Jupyter notebook działa
- [ ] `test.ipynb` uruchomiony (lub używasz przykładowych danych)
- [ ] `analysis_patterns.ipynb` uruchomiony
- [ ] 10 plików w `saved_responses/`
- [ ] `python quick_summary.py` działa
- [ ] Przeczytany `README.md` + `FINAL_SUMMARY.md`

---

## 🎓 Support

Jeśli coś nie działa:
1. Sprawdź requirements: Python 3.12+, Google API Key
2. Zobacz `README.md` - sekcja Troubleshooting
3. Sprawdź błędy w `get_errors()` (VS Code)
4. Użyj przykładowych danych zamiast API calls (szybciej)

---

**Powodzenia!** 🚀

Czas setup: ~15 minut (z przykładowymi danymi) lub ~1 godzina (z własnymi API calls)
