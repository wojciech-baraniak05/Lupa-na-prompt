# Lupa na Prompt - Analiza wpływu zmian promptu na odpowiedzi LLM
W projekcie LLM służy do badania jak zmiany w promptach mogą wpłynąć na zmianę odpowiedzi. 
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

**Dashboard porównawczy (Gemma vs LLaMA):**
```powershell
# Upewnij się, że środowisko jest aktywne
.\.venv\Scripts\Activate.ps1

# Uruchom aplikację Streamlit
streamlit run strona.py
```

Aplikacja otworzy się automatycznie w przeglądarce pod adresem `http://localhost:8501`

### Struktura projektu

- `gemma_generation.ipynb` / `llama_generation.ipynb` - Generowanie odpowiedzi dla modeli
- `analysis_patterns.ipynb` / `analysis_patterns_llama.ipynb` - Analiza wzorców odpowiedzi
- `strona.py` - Główny, łączony dashboard Streamlit (Gemma vs LLaMA)
- `prompts2.csv` - Dane wejściowe z promptami
- `saved_responses/` oraz `saved_responses_llama/` - Zapisane odpowiedzi modeli
- `results_gemini/` oraz `results_llama/` - Wyeksportowane wyniki analiz

