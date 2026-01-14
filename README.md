# Lupa na Prompt - Analiza wpływu zmian promptu na odpowiedzi LLM

## Jak uruchomić projekt?

### Inicjalizacja środowiska

```powershell
# Utwórz wirtualne środowisko Python
python -m venv .venv

# Aktywuj środowisko
.\.venv\Scripts\Activate.ps1

# Zainstaluj zależności z pliku requirements.txt
pip install -r requirements.txt
```

### Konfiguracja tokenów API

Utwórz plik `tokens.env` w głównym katalogu projektu i dodaj swoje klucze API:

```
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```


### Uruchamianie aplikacji Streamlit

**Strona Gemma (strona_gemma.py):**
```powershell
# Upewnij się, że środowisko jest aktywne
.\.venv\Scripts\Activate.ps1

# Uruchom aplikację Streamlit
streamlit run strona_gemma.py
```

Aplikacja otworzy się automatycznie w przeglądarce pod adresem `http://localhost:8501`

### Struktura projektu

- `gemma_generation.ipynb` - Generowanie odpowiedzi za pomocą modelu Gemma
- `analysis_patterns.ipynb` - Analiza wzorców odpowiedzi
- `analysis_patterns_groq.ipynb` - Analiza wzorców dla modelu Groq
- `strona_gemma.py` - Interaktywny dashboard Streamlit z wynikami
- `prompts.csv` / `prompts2.csv` - Dane wejściowe z promptami
- `saved_responses/` - Zapisane odpowiedzi modeli
- `saved_responses_groq/` - Zapisane odpowiedzi modeli Groq
- `results_gemini/` - Wyeksportowane wyniki analiz

