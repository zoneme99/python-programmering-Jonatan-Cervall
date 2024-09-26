import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("Labs/datapoints.csv")

colors = {1: 'blue', 0: 'orange'}
color_list = [colors[group] for group in df['(0-pichu 1-pikachu)']]


plt.scatter(df["width (cm)"],df["height (cm)"], c = color_list)

pattern = re.compile(r'\(([^)]*)\)')

with open("Labs/testpoints.txt", "r") as file:
    testdata = pattern.findall(file.read())

finedata = list()
for data in testdata:
    temp = data.split(",")
    x = float(temp[0])
    y = float(temp[1])
    finedata.append([x,y])

point_index = list()
for data in finedata:
    testwidth = np.array(list(map(lambda x: np.pow(x - data[0], 2), df["width (cm)"])))
    testheight = np.array(list(map(lambda x: np.pow(x - data[1], 2), df["height (cm)"])))
    distance = np.sqrt(np.add(testwidth, testheight))
    point_index.append(np.argmin(distance))


pokemons = [df["(0-pichu 1-pikachu)"][index] for index in point_index]

colors = {1: 'green', 0: 'red'}
color_list = [colors[group] for group in pokemons]

x = [data[0] for data in finedata]
y = [data[1] for data in finedata]
plt.scatter(x, y, c = color_list)



plt.show()