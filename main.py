# from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np
# from transformers import pipeline
from src.lupa.Model import DataModel
import pandas as pd


import pandas as pd
def main():
    print("wykonano importy")
    df = pd.read_csv("prompts2.csv", sep=";")
    X, y = df['Prompt'].values, df['Flag'].values
    print(type(X))
    data_model = DataModel(X, y)
    print(data_model)




if __name__ == "__main__":
    main()
