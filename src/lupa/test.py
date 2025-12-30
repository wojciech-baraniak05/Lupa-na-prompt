import pandas as pd

x = [1,2,3,4]
print(x)
x = pd.Series(x)
def dupa(x):
    return 2*x+1
print(dupa(x))