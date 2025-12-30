# 📁 MANIFEST PROJEKTU - "Lupa na Prompt"

**Data finalizacji:** 2025-12-30  
**Status:** ✅ UKOŃCZONY

---

## 📊 Statystyki projektu

- **Pliki główne:** 13
- **Notebooks:** 7 (2 główne + 5 testowych/backup)
- **Dokumentacja:** 8 plików
- **Wyniki:** 10 plików CSV/JSON
- **Skrypty pomocnicze:** 3
- **Całkowity rozmiar (saved_responses):** ~0.11 MB

---

## 🗂️ Struktura plików

### 1️⃣ NOTEBOOKS GŁÓWNE (2)

#### `test.ipynb` - ETAP 1: Zbieranie danych
- **Status:** ✅ Ukończony, wszystkie testy przechodzą
- **Rozmiar:** ~10 komórek
- **Funkcje:**
  - DataModel class z rate limiting (15 req/min)
  - 12 strategii promptowania
  - 720 API calls do Gemma 3.4B
  - Parsowanie odpowiedzi (0/1/NaN)
  - Metryki: Accuracy, Precision, Recall, F1
  - Diagnostyka + wizualizacje
- **Output:** raw_responses, parsed_responses, controversial, metrics

#### `analysis_patterns.ipynb` - ETAP 2: Analiza wzorców
- **Status:** ✅ Ukończony, 19 komórek executed (counts 37-49)
- **Rozmiar:** 19 komórek kodu
- **Funkcje:**
  - Wczytanie danych z ETAP 1
  - Macierz zmienności (transition matrix)
  - Interaktywny dashboard (ipywidgets)
  - Pattern analysis X→Y
  - Detekcja halucynacji (TOP 25% threshold)
  - Risk scoring per strategy
  - Export CSV + JSON
- **Output:** ranking, transition_matrix, hallucination_cases, risk_indicators, variability_analysis, report.json

---

### 2️⃣ NOTEBOOKS TESTOWE/BACKUP (5)

- `testV2.ipynb` - Alternatywna wersja test.ipynb z retry logic
- `test2.ipynb` - Backup
- `testWojtka.ipynb` - Testowa wersja
- `testOby.ipynb` - Backup
- `test — kopia.ipynb` - Kopia zapasowa

**Uwaga:** Te notebooki mogą zawierać przestarzały kod lub błędy - używaj głównych wersji.

---

### 3️⃣ DANE WEJŚCIOWE (2)

#### `prompts.csv`
- **Rozmiar:** Nieznany (starsze dane)
- **Format:** CSV z kolumnami Prompt, Flag
- **Status:** DEPRECATED - używaj prompts2.csv

#### `prompts2.csv`
- **Rozmiar:** ~60 wierszy
- **Format:** CSV z kolumnami Prompt, Flag
- **Zawartość:**
  - 60 zdań matematycznych
  - 30 prawdziwych (Flag=1)
  - 30 fałszywych (Flag=0)
- **Używany przez:** test.ipynb, testV2.ipynb

---

### 4️⃣ WYNIKI ANALIZY (10 plików w saved_responses/)

#### A. Dane surowe z ETAP 1 (4 pliki)

1. **`raw_responses_2025-12-30_20-51-50.csv`** (84,225 bytes)
   - Pełne odpowiedzi z API Gemma 3.4B
   - 720 wierszy (60 promptów × 12 strategii)
   - Kolumny: Prompt, Strategy, Response, Flag, Timestamp

2. **`parsed_responses_2025-12-30_20-51-50.csv`** (2,098 bytes)
   - Sparsowane odpowiedzi do formatu binarnego
   - Kolumny: Prompt × 12 strategii (0/1/NaN)
   - **Używany przez:** analysis_patterns.ipynb

3. **`controversial_2025-12-30_22-54-24.csv`** (6,675 bytes)
   - Kontrowersyjne przypadki (wysokie konflikty)
   - Przypadki gdzie strategie się nie zgadzają
   - Diagnostyka problemów z modelem

4. **`metrics_2025-12-30_22-54-24.csv`** (389 bytes)
   - Metryki per strategia
   - Kolumny: Strategy, Accuracy, Precision, Recall, F1

#### B. Wyniki z ETAP 2 (6 plików)

5. **`ranking_strategies_2025-12-30_22-57-21.csv`** (993 bytes)
   - Ranking strategii od best do worst
   - Kolumny: Strategy, Accuracy, Rank

6. **`transition_matrix_2025-12-30_22-57-21.csv`** (2,995 bytes)
   - Macierz zmian między strategiami
   - % przypadków gdzie odpowiedź się zmienia
   - Heatmapa używana w Cell 6

7. **`hallucination_cases_2025-12-30_22-57-21.csv`** (1,791 bytes)
   - TOP przypadki halucynacji
   - Threshold: std dev > 0.5
   - Kolumny: Idx, Prompt, True, Std, Consensus, Hallucination_Risk, Error_Rate

8. **`risk_indicators_2025-12-30_22-57-21.csv`** (646 bytes)
   - Risk scoring per strategy
   - Kolumny: Strategy, Hallucination_Risk, Base_Accuracy

9. **`variability_analysis_2025-12-30_22-57-21.csv`** (6,372 bytes)
   - Zmienność per prompt
   - Kolumny: Idx, Prompt, True, N_Strategies, Unique_Preds, Has_Conflict, Std, Consensus

10. **`report_2025-12-30_22-57-21.json`** (1,233 bytes)
    - Strukturalny raport końcowy
    - Zawiera: metadata, summary, patterns, recommendations
    - Format JSON - łatwy do parsowania

---

### 5️⃣ DOKUMENTACJA (8 plików)

#### `README.md` (główny)
- **Status:** ✅ Zaktualizowany (merged z README_NEW.md)
- **Zawartość:**
  - Cel projektu
  - Quick start (3 kroki)
  - Struktura projektu
  - Wyniki + rekomendacje
  - Setup instructions
  - Troubleshooting

#### `README_NEW.md`
- **Status:** DEPRECATED (treść przeniesiona do README.md)
- Backup nowej wersji dokumentacji

#### `README_OLD.md`
- **Status:** DEPRECATED (backup starego README)
- Zawiera tylko setup instructions (uv sync)

#### `INSTRUKCJA_PROJEKTУ.md`
- **Rozmiar:** 210 linii
- **Zawartość:**
  - Szczegółowa instrukcja techniczna (5 sekcji)
  - ETAP 1: Metodologia zbierania danych
  - ETAP 2: Struktura analizy
  - 12 strategii promptowania (opisy)
  - Output files format

#### `TODO.md`
- **Status:** ✅ Zaktualizowany (100% complete)
- **Zawartość:**
  - Wykonane zadania (ETAP 1 + ETAP 2)
  - Opcjonalne zadania (ETAP 3-5, nie zrealizowane)
  - Status końcowy + główne wnioski

#### `CHECKLIST_ZAKONCZENIA.md`
- **Status:** ✅ Zaktualizowany (wszystkie checklist ✅)
- **Zawartość:**
  - Status ukończonych zadań
  - TOP 5 discoveries
  - Rekomendacje
  - Metryki końcowe

#### `FINAL_SUMMARY.md`
- **Rozmiar:** ~300 linii
- **Zawartość:**
  - Kompletne podsumowanie projektu
  - Co zostało osiągnięte (ETAP 1 + 2)
  - TOP 5 wniosków z analizy
  - Rekomendacje dla Gemmy 3.4B
  - Metryki końcowe
  - Wnioski naukowe
  - Checklist zakończenia

#### `PREZENTACJA.md`
- **Rozmiar:** ~250 linii
- **Zawartość:**
  - Instrukcja prezentacji (8 slajdów)
  - Timeline (9-10 min)
  - Demo live (3 opcje)
  - FAQ + spodziewane pytania
  - Checklist przed prezentacją

---

### 6️⃣ SKRYPTY POMOCNICZE (3)

#### `main.py`
- **Status:** Nieużywany (projekt używa Jupyter notebooks)
- Prawdopodobnie stary entry point

#### `quick_summary.py`
- **Status:** ✅ Działa poprawnie
- **Funkcje:**
  - Wczytuje najnowszy report JSON
  - Wyświetla podsumowanie wyników w terminalu
  - TOP 5 zmian, halucynacji, ryzyka
- **Użycie:** `python quick_summary.py`

#### `cleanup_duplicates.py`
- **Status:** ✅ Działa poprawnie
- **Funkcje:**
  - Usuwa starsze duplikaty raportów
  - Zachowuje tylko najnowsze wersje
  - Automatyczna detekcja timestamps
- **Użycie:** `python cleanup_duplicates.py`
- **Efekt:** Usunęło 6 starych plików (22-49-38 timestamp)

---

### 7️⃣ KONFIGURACJA (2)

#### `pyproject.toml`
- **Zawartość:** Konfiguracja projektu Python
- Dependencies: pandas, numpy, matplotlib, seaborn, ipywidgets, scikit-learn, google-generativeai

#### `.venv/` (folder)
- Virtual environment Python 3.12.7
- Wszystkie zależności zainstalowane

---

### 8️⃣ KONTEKST (2 pliki w context/)

#### `context/MN.md`
- Kontekst matematyczny dla modelu
- Wykłady/materiały do analizy

#### `context/prob.md`
- Prawdopodobnie materiały do probabilistyki

---

### 9️⃣ ŹRÓDŁA (1)

#### `src/lupa/`
- **Model.py** - Klasa DataModel (może być duplikatem z notebooka)
- **test.py** - Testy jednostkowe
- **__init__.py** - Package init
- **Status:** Prawdopodobnie nieużywany (projekt głównie w Jupyter)

---

## ✅ Pliki gotowe do prezentacji/publikacji

### Główne (MUST-HAVE):
1. ✅ `README.md` - dokumentacja użytkownika
2. ✅ `test.ipynb` - ETAP 1 (zbieranie danych)
3. ✅ `analysis_patterns.ipynb` - ETAP 2 (analiza)
4. ✅ `prompts2.csv` - dane wejściowe
5. ✅ `saved_responses/report_2025-12-30_22-57-21.json` - raport końcowy
6. ✅ `FINAL_SUMMARY.md` - podsumowanie wyników

### Dodatkowe (NICE-TO-HAVE):
7. ✅ `INSTRUKCJA_PROJEKTУ.md` - instrukcja techniczna
8. ✅ `PREZENTACJA.md` - jak prezentować projekt
9. ✅ `quick_summary.py` - szybkie podsumowanie
10. ✅ `cleanup_duplicates.py` - utility do czyszczenia

### Pliki robocze (można pominąć):
- testV2.ipynb, test2.ipynb, testOby.ipynb, testWojtka.ipynb, test — kopia.ipynb
- README_OLD.md, README_NEW.md
- prompts.csv (starsza wersja)
- src/lupa/ (nieużywany)

---

## 📊 Podsumowanie zawartości

### Co projekt robi:
- Testuje 12 strategii promptowania na Gemma 3.4B
- Zbiera 720 odpowiedzi z API
- Analizuje zmienność i halucynacje
- Generuje ranking strategii
- Identyfikuje najbardziej ryzykowne modyfikacje

### Główne wnioski:
1. **Baseline (65%) > wszystkie inne strategie**
2. **Scramble = -14pp** (największa katastrofa)
3. **Expert Role = -11.7pp** (paradoks)
4. **75% promptów** ma konflikty
5. **Gemma 3.4B bardzo niestabilna** dla małych zmian

### Gotowość:
- ✅ Kod działa bez błędów
- ✅ Wszystkie analizy ukończone
- ✅ Dokumentacja kompletna
- ✅ Wyniki wyeksportowane
- ✅ Prezentacja przygotowana

---

**Projekt READY FOR SUBMISSION** 🚀
