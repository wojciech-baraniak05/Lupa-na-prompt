import numpy as np
import pandas as pd
import string
from random import sample, choice
class DataModel:
    def __init__(self, df):
        self.df = df
    def __call__(self):
        print(f"DataModel(X={self.df.shape})")
        print(f"Columns: {self.df.columns.to_list()}")
        print(f"Prompt: \n {self.df["Prompt"].head(2).to_list()}")
        print(f"Flag: \n {self.df["Flag"].head(2).to_list()}")
    def make_prompts(self):
        self.df["Prompt"] = self.df["Prompt"].apply(lambda x: f"Odpowiedz 0 jeśli zdanie jest fałszywe, a 1 jeśli prawdziwe: {x}")
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
            'Negative_prompt': lambda x: f"Myślę, że to zdanie zawiera problem, czy mam rację?: {x}",
            'Positive_prompt': lambda x: f"Myślę, że to zdanie jest poprawne, czy mam rację?: {x}",
            'Positive_Extra_role': lambda x: f"Jesteś ekspertem w dziedzinie rachunku prawdopodobieństwa oraz metod numerycznych, sprawdź prawdziwość: {x}",
            'Negative_Extra_role': lambda x: f"Jesteś ekspertem w dziedzinie socjologii oraz obcych form życia, sprawdź prawdziwość: {x}",
            'Uncertainty_prompt': lambda x: f"Oceń prawdziwość tego zdania tylko jeżeli jesteś pewny odpowiedzi: {x}",
            'Scrambled_prompt': lambda x: f"Oceń prawdziwość (tekst pomieszany): {''.join(np.random.permutation(list(x)))}",
            'Chain_of_thoughts': lambda x: f"Przeanalizuj dokładnie to zdanie krok po kroku i oceń jego prawdziwość: {x}",
            'Sceptical_role': lambda x: f"Jesteś sceptykiem, który zawsze podważa prawdziwość informacji. Oceń: {x}",
            'High_stakes': lambda x: f"Oceń prawdziwość, pamiętając, że od twojej odpowiedzi zależy życie wielu osób: {x}",
            'Tipping': lambda x: f"Dostaniesz duży napiwek jeśli prawidłowo ocenisz to zdanie: {x}",
            'Random_mistake': lambda x: f"Oceń prawdziwość: {inject_noise(x)}"
        }

        for col_name, func in strategies.items():
            self.df[col_name] = self.df["Prompt"].apply(func)
