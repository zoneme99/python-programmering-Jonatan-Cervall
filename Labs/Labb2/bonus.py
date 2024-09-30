import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Labs/Labb2/datapoints.csv")

df = df.sample(frac = 1)

find = 25

#print(df["(0-pichu 1-pikachu)"][3])

def find_pokemon_index(dataseries, pokemon, to_find):
    pokemon_indices = list()
    for index in dataseries.index:
        if dataseries[index] == pokemon:
            pokemon_indices.append(index)
    return pokemon_indices

lst = find_pokemon_index(df["(0-pichu 1-pikachu)"], 1, 10)
print(len(lst))