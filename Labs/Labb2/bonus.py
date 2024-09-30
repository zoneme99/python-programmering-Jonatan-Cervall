import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Labs/Labb2/datapoints.csv")

df = df.sample(frac = 1)

find = 50

#print(df["(0-pichu 1-pikachu)"][3])

def data_seperation(dataframe, to_find):
    test_pokemons = pd.DataFrame()
    train_pokemons = pd.DataFrame()
    pikachu = 0
    pichu = 0
    for index, row in dataframe.iterrows():
        if pikachu < (to_find / 2):
            test_pokemons = pd.concat([test_pokemons, row.to_frame().T])
            pikachu += 1
        elif pichu < (to_find / 2):
            test_pokemons = pd.concat([test_pokemons, row.to_frame().T])
            pichu += 1
        else:
            train_pokemons = pd.concat([train_pokemons, row.to_frame().T])
    return test_pokemons, train_pokemons

test, train = data_seperation(df, find)

print(test)
print(len(train))
