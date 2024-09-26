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

def edistance(xwid, yhei , widlist, heilist):
    width = np.array(list(map(lambda x: np.pow(x - xwid, 2), widlist)))
    height = np.array(list(map(lambda x: np.pow(x - yhei, 2), heilist)))
    distance = np.sqrt(np.add(width, height))
    return np.argmin(distance)

point_index = list()
for data in finedata:
    point_index.append(edistance(data[0], data[1], df["width (cm)"], df["height (cm)"]))


pokemons = [df["(0-pichu 1-pikachu)"][index] for index in point_index]

colors = {1: 'green', 0: 'red'}
color_list = [colors[group] for group in pokemons]

x = [data[0] for data in finedata]
y = [data[1] for data in finedata]
plt.scatter(x, y, c = color_list)

for index, data in enumerate(finedata):
    print("Sample with (width, height): ({data0}, {data1}) classified as {pokemon}".format(data0 = data[0], data1 = data[1], pokemon = "Pikachu" if df["(0-pichu 1-pikachu)"][point_index[index]] == 1 else "Pichu"))

while True:
    try:
        inpx = float(input("Insert width of pokemon: "))
        if inpx >= 0:
            break
        else:
            print("wrong input, negative values not allowed")
    except ValueError:
        print("wrong input, test again")

while True:
    try:
        inpy = float(input("Insert width of pokemon: "))
        if inpy >= 0:
            break
        else:
            print("wrong input, negative values not allowed")
    except ValueError:
        print("wrong input, test again")

indexpoint = edistance(inpx, inpy, df["width (cm)"], df["height (cm)"])

print("IT IS A {pokemon}".format(pokemon = "Pikachu" if df["(0-pichu 1-pikachu)"][indexpoint] == 1 else "Pichu"))
plt.scatter(inpx, inpy, c = "black")

def edistance10(xwid, yhei , widlist, heilist, label):
    width = np.array(list(map(lambda x: np.pow(x - xwid, 2), widlist)))
    height = np.array(list(map(lambda x: np.pow(x - yhei, 2), heilist)))
    distance = pd.Series(np.sqrt(np.add(width, height)))
    mean = list()
    for _ in range(10):
        mean.append([distance.argmin, distance[distance.argmin]])
        distance.drop(distance.argmin) #BÖRJA HÄÄÄÄÄÄRRRRR
    #return np.argmin(distance)

plt.show()