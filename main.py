# from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np
from transformers import pipeline

import pandas as pd
def main():
    print("wykonano importy")
    pipe_mod = pipeline("sentiment-analysis")
    res = pipe_mod("dupsko 1234")
    print(res)


if __name__ == "__main__":
    main()
