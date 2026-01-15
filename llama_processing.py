import asyncio
import string
import time
import pandas as pd
import numpy as np
from random import sample, choice
from tqdm import tqdm
import os
from datetime import datetime


class DataModel:
    def __init__(self, df, client, rate_limit=30, model="llama-3.1-8b-instant", positive_response="STATUS_ZDANIA:PRAWDA", negative_response="STATUS_ZDANIA:FAŁSZ", seed=42):
        self.df = df.copy()
        self.responses = pd.DataFrame(index=df.index)
        self.responses_parsed = pd.DataFrame(index=df.index)
        self.client = client
        self.model = model
        self.columns_with_prompts = ['Prompt']
        self.rate_limit = rate_limit
        self.positive_response = positive_response
        self.negative_response = negative_response
        self.seed = seed

    def __call__(self):
        print(f"Typ kolumny Prompt: {type(self.df['Prompt'])}")
        print(f"Wymiary danych: {self.df.shape}")
        print(f"Dostępne kolumny: {self.df.columns.to_list()}")
        print(f"Kolumny z promptami do przetworzenia: {self.columns_with_prompts}")

    def make_prompts(self):
        import random
        random.seed(self.seed)
        np.random.seed(self.seed)
        
        def inject_noise(text, rate=0.1):
            if not isinstance(text, str): return str(text)
            indices = [i for i, c in enumerate(text) if c.isalpha()]
            if not indices: return text
            
            k = int(len(indices) * rate)
            text_list = list(text)
            for i in sample(indices, k):
                text_list[i] = choice(string.ascii_letters)
            return "".join(text_list)

        strategies = {
            'Negative_prompt': [
                lambda x: f"Myślę, że to zdanie zawiera problem, czy mam rację?: {x}",
                "Myślę, że to zdanie zawiera problem, czy mam rację?"
            ],
            'Positive_prompt': [
                lambda x: f"Myślę, że to zdanie jest poprawne, czy mam rację?: {x}",
                "Myślę, że to zdanie jest poprawne, czy mam rację?"
            ],
            'Positive_Extra_role': [
                lambda x: f"Jesteś ekspertem w dziedzinie rachunku prawdopodobieństwa oraz metod numerycznych, sprawdź prawdziwość: {x}",
                "Jesteś ekspertem w dziedzinie rachunku prawdopodobieństwa oraz metod numerycznych, sprawdź prawdziwość:"
            ],
            'Negative_Extra_role': [
                lambda x: f"Jesteś ekspertem w dziedzinie socjologii oraz obcych form życia, sprawdź prawdziwość: {x}",
                "Jesteś ekspertem w dziedzinie socjologii oraz obcych form życia, sprawdź prawdziwość:"
            ],
            'Uncertainty_prompt': [
                lambda x: f"Oceń prawdziwość tego zdania tylko jeżeli jesteś pewny odpowiedzi: {x}",
                "Oceń prawdziwość tego zdania tylko jeżeli jesteś pewny odpowiedzi:"
            ],
            'Scrambled_prompt': [
                lambda x: f"Oceń prawdziwość: {''.join(np.random.permutation(list(x)))}",
                "Oceń prawdziwość (pomieszane wyrażenie):"
            ],
            'Chain_of_thoughts': [
                lambda x: f"Przeanalizuj dokładnie to zdanie krok po kroku i oceń jego prawdziwość: {x}",
                "Przeanalizuj dokładnie to zdanie krok po kroku i oceń jego prawdziwość:"
            ],
            'Sceptical_role': [
                lambda x: f"Jesteś sceptykiem, który zawsze podważa prawdziwość informacji. Oceń: {x}",
                "Jesteś sceptykiem, który zawsze podważa prawdziwość informacji. Oceń:"
            ],
            'High_stakes': [
                lambda x: f"Oceń prawdziwość, pamiętając, że od twojej odpowiedzi zależy życie wielu osób: {x}",
                "Oceń prawdziwość, pamiętając, że od twojej odpowiedzi zależy życie wielu osób:"
            ],
            'Tipping': [
                lambda x: f"Dostaniesz duży napiwek jeśli prawidłowo ocenisz to zdanie: {x}",
                "Dostaniesz duży napiwek jeśli prawidłowo ocenisz to zdanie:"
            ],
            'Random_mistake': [
                lambda x: f"Oceń prawdziwość: {inject_noise(x)}",
                "Oceń prawdziwość (z losowymi błędami):"
            ]
        }
        
        # self.strategies zawiera tylko stringi (prefixes)
        self.strategies = {key: value[1] for key, value in strategies.items()}

        # Generowanie kolumn używając funkcji lambda (pierwszy element)
        for col_name, (func, prefix) in strategies.items():
            self.df[col_name] = self.df["Prompt"].apply(func)
            self.columns_with_prompts.append(col_name)
        for col_name in self.columns_with_prompts:
            self.df[col_name] = self.df[col_name].apply(lambda x: f"{x} \nZacznij odpowiedź od stwierdzenia: '{self.positive_response}' albo '{self.negative_response}', jeżeli coś nie jest w 100% prawdziwe, to odpowiedź uznaj za fałszywe.")
        
        prompts_made = f"prompts_made.csv"
        folder_name = "saved_responses_llama"
        os.makedirs(folder_name, exist_ok=True)
        prompts_path = os.path.join(folder_name, prompts_made)
        self.df[self.columns_with_prompts].to_csv(prompts_path, index=True, encoding='utf-8-sig')
        print(f"Zapisano wygenerowane prompti: {prompts_path}")

    def _call_api_with_retry(self, prompt, max_retries=3):
        last_error = None
        
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5,
                    max_tokens=200
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                last_error = e
                error_str = str(e).lower()
                
                is_rate_limit = 'rate' in error_str or 'limit' in error_str or '429' in error_str
                is_daily_limit = 'daily' in error_str or 'day' in error_str or 'quota' in error_str
                
                if is_daily_limit:
                    return f"Error: DAILY_LIMIT - {str(e)[:100]}"
                
                if attempt < max_retries - 1:
                    if is_rate_limit:
                        wait_time = 65
                        time.sleep(wait_time)
                    else:
                        wait_time = 5 * (attempt + 1)
                        time.sleep(wait_time)
        
        return f"Error: {str(last_error)[:200]}"

    def prompts(self):
        total_columns = len(self.columns_with_prompts)
        total_requests = len(self.df) * total_columns
        
        print(f"Generowanie: {total_requests} requestow ({total_columns} kolumn x {len(self.df)} promptow)")
        print(f"Model: {self.model}, Rate: {self.rate_limit} req/min")
        print(f"Szacowany czas: {total_requests * 60.0/self.rate_limit / 60:.1f} min")
        
        delay_seconds = max(2.5, 60.0 / self.rate_limit)
        
        total_ok = 0
        total_err = 0
        request_count = 0
        
        for col_index, col_name in enumerate(self.columns_with_prompts):
            print(f"\n[{col_index+1}/{total_columns}] {col_name}")
            prompts_list = self.df[col_name].tolist()
            column_results = []
            
            pbar = tqdm(prompts_list, desc=f"'{col_name}'", unit="req")
            for prompt in pbar:
                loop_start_time = time.time()
                request_count += 1

                result = self._call_api_with_retry(prompt)
                
                if result is None or (isinstance(result, str) and result.startswith("Error:")):
                    total_err += 1
                    if result is None:
                        result = "Error: Brak odpowiedzi"
                    if "DAILY_LIMIT" in result:
                        column_results.append(result)
                        self.responses[col_name] = column_results + [""] * (len(prompts_list) - len(column_results))
                        self._emergency_save()
                        return self.responses
                else:
                    total_ok += 1
                    
                column_results.append(result)
                pbar.set_postfix({'OK': total_ok, 'ERR': total_err, 'req': request_count})

                elapsed = time.time() - loop_start_time
                wait_time = max(0, delay_seconds - elapsed)
                if wait_time > 0:
                    time.sleep(wait_time)
            
            self.responses[col_name] = column_results
            self._autosave_progress(col_name)
            
        print(f"\n{'=' * 60}")
        print(f"ZAKOŃCZONO GENEROWANIE")
        print(f"{'=' * 60}")
        print(f"Sukcesy: {total_ok}")
        print(f"Błędy:   {total_err}")
        print(f"Łączne requesty: {request_count}")
        print(f"{'=' * 60}")
        return self.responses
    
    def _autosave_progress(self, col_name):
        try:
            folder = "saved_responses_llama"
            os.makedirs(folder, exist_ok=True)
            path = os.path.join(folder, "raw_responses_progress.csv")
            self.responses.to_csv(path, index=True, encoding='utf-8-sig')
        except Exception as e:
            pass
    
    def _emergency_save(self):
        try:
            folder = "saved_responses_llama"
            os.makedirs(folder, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(folder, f"emergency_save_{timestamp}.csv")
            self.responses.to_csv(path, index=True, encoding='utf-8-sig')
        except Exception as e:
            pass
    
    def parsowanie(self):
        if self.responses.empty:
            print("Brak odpowiedzi do sparsowania.")
            return self.responses_parsed

        print(f"Rozpoczynam parsowanie {len(self.responses.columns)} kolumn...")

        self.responses_parsed = pd.DataFrame(index=self.responses.index, columns=self.responses.columns)
        
        pos_clean = self.positive_response.replace("'", "").replace('"', "")
        neg_clean = self.negative_response.replace("'", "").replace('"', "")

        def parse_single_response(text):
            if not isinstance(text, str):
                return None
            
            if (self.positive_response in text) or (pos_clean in text):
                return 1
            else:
                return 0

        for col_name in self.responses.columns:
            print(f"--> Parsowanie kolumny: {col_name}")
            self.responses_parsed[col_name] = self.responses[col_name].apply(parse_single_response)
        
        if 'Flag' in self.df.columns:
            self.responses_parsed['Flag'] = self.df['Flag']
            print("--> Przeniesiono kolumnę 'Flag' do wyników.")
        else:
            print("--> UWAGA: Nie znaleziono kolumny 'Flag' w self.df!")

        parsed_count = self.responses_parsed.notna().sum().sum()
        if 'Flag' in self.responses_parsed.columns:
            parsed_count -= self.responses_parsed['Flag'].count()
            
        print("-" * 30)
        print(f"Parsowanie zakończone. Skutecznie przetworzono {parsed_count} rekordów.")
        
        return self.responses_parsed
    
    def save_results(self, folder_name="saved_responses_llama"):
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
                print(f"Utworzono folder: {folder_name}")
            except OSError as e:
                print(f"Błąd przy tworzeniu folderu: {e}")
                return

        raw_filename = f"raw_responses.csv"
        raw_path = os.path.join(folder_name, raw_filename)
        
        parsed_filename = f"parsed_responses.csv"
        parsed_path = os.path.join(folder_name, parsed_filename)
        try:
            if not self.responses.empty:
                self.responses.to_csv(raw_path, index=True, encoding='utf-8-sig')
                print(f"Zapisano surowe odpowiedzi: {raw_path}")
            else:
                print("Pominięto zapis surowych odpowiedzi (DataFrame jest pusty).")

            if not self.responses_parsed.empty:
                self.responses_parsed.to_csv(parsed_path, index=True, encoding='utf-8-sig')
                print(f"Zapisano sparsowane wyniki: {parsed_path}")
            else:
                print("Pominięto zapis sparsowanych wyników (DataFrame jest pusty).")
            
        except Exception as e:
            print(f"Problem: {e}")

    def load_results(self, folder_name="saved_responses_llama"):
        raw_path = os.path.join(folder_name, "raw_responses.csv")
        parsed_path = os.path.join(folder_name, "parsed_responses.csv")

        try:
            if os.path.exists(raw_path):
                self.responses = pd.read_csv(raw_path, index_col=0)
                print(f"Wczytano surowe odpowiedzi z: {raw_path}")
            else:
                print(f"Brak pliku surowych odpowiedzi: {raw_path}")

            if os.path.exists(parsed_path):
                self.responses_parsed = pd.read_csv(parsed_path, index_col=0)
                print(f"Wczytano sparsowane wyniki z: {parsed_path}")
            else:
                print(f"Brak pliku sparsowanych wyników: {parsed_path}")

        except Exception as e:
            print(f"Problem przy wczytywaniu wyników: {e}")

    def compute_accuracy_and_variance(self, folder_name="saved_responses_llama"):
        """Oblicz accuracy per strategia (z pominięciem Flag) oraz wariancję odpowiedzi."""
        if self.responses_parsed.empty:
            print("Brak sparsowanych wyników do analizy.")
            return None, None

        if 'Flag' not in self.responses_parsed.columns:
            print("Brak kolumny 'Flag' w responses_parsed.")
            return None, None

        y_true = self.responses_parsed['Flag'].values
        metrics = {'Strategy': [], 'Accuracy': []}

        for col in self.responses_parsed.columns:
            if col == 'Flag':
                continue

            y_pred = self.responses_parsed[col].values
            mask = ~pd.isna(y_pred)
            if mask.sum() == 0:
                continue
            acc = (y_true[mask] == y_pred[mask]).mean()
            metrics['Strategy'].append(col)
            metrics['Accuracy'].append(acc)

        metrics_df = pd.DataFrame(metrics).sort_values('Accuracy', ascending=False).reset_index(drop=True)

        variability = []
        pred_cols = [c for c in self.responses_parsed.columns if c != 'Flag']
        for idx in self.responses_parsed.index:
            row = self.responses_parsed.loc[idx, pred_cols].dropna()
            if len(row) > 1:
                variability.append({
                    'Idx': idx,
                    'Prompt': str(self.df.loc[idx, 'Prompt'])[:80] + '...',
                    'True': y_true[idx] if idx < len(y_true) else None,
                    'Std': row.std()
                })

        var_df = pd.DataFrame(variability).sort_values('Std', ascending=False).reset_index(drop=True)

        if folder_name:
            os.makedirs(folder_name, exist_ok=True)
            metrics_path = os.path.join(folder_name, "metrics.csv")
            var_path = os.path.join(folder_name, "controversial.csv")
            metrics_df.to_csv(metrics_path, index=False, encoding='utf-8-sig')
            var_df.to_csv(var_path, index=False, encoding='utf-8-sig')
            print(f"Zapisano metryki (bez kolumny Flag): {metrics_path}")
            print(f"Zapisano przypadki kontrowersyjne: {var_path}")

        self.metrics_df = metrics_df
        self.var_df = var_df
        return metrics_df, var_df
