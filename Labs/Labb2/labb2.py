import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("Labs/Labb2/datapoints.csv")


pikachu = df.loc[df["(0-pichu 1-pikachu)"] == 1]
pichu = df.loc[df["(0-pichu 1-pikachu)"] == 0]

plt.scatter(pikachu["width (cm)"],pikachu["height (cm)"], color= "blue")
plt.scatter(pichu["width (cm)"],pichu["height (cm)"], color= "orange")


pattern = re.compile(r'\(([^)]*)\)')

with open("Labs/Labb2/testpoints.txt", "r") as file:
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


pokemons = [df.loc[index] for index in point_index]
pokemons = pd.DataFrame(pokemons)
pikachus = list()
pichus = list()
for index, poke in enumerate(pokemons["(0-pichu 1-pikachu)"]):
    if int(poke) == 1:
        pikachus.append(finedata[index])
    else:
        pichus.append(finedata[index])


xpik = [data[0] for data in pikachus]
ypik = [data[1] for data in pikachus]
xpic = [data[0] for data in pichus]
ypic = [data[1] for data in pichus]
plt.scatter(xpik, ypik, color = "green")
plt.scatter(xpic, ypic, color = "red")

for index, data in enumerate(finedata):
    print("Sample with (width, height): ({data0}, {data1}) classified as {pokemon}".format(data0 = data[0], data1 = data[1], pokemon = "Pikachu" if df["(0-pichu 1-pikachu)"][point_index[index]] == 1 else "Pichu"))

print("Insert dimensions for pokemon(closest neighbor, black dot):")

def inputs():
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
            inpy = float(input("Insert height of pokemon: "))
            if inpy >= 0:
                break
            else:
                print("wrong input, negative values not allowed")
        except ValueError:
            print("wrong input, test again")
    return inpx, inpy

inpx, inpy = inputs()

indexpoint = edistance(inpx, inpy, df["width (cm)"], df["height (cm)"])
predict1 = "Pikachu" if df["(0-pichu 1-pikachu)"][indexpoint] == 1 else "Pichu"
print(f"IT IS A {predict1}")
plt.scatter(inpx, inpy, c = "black")

def edistance10(xwid, yhei , widlist, heilist, label):
    width = np.array(list(map(lambda x: np.pow(x - xwid, 2), widlist)))
    height = np.array(list(map(lambda x: np.pow(x - yhei, 2), heilist)))
    distance = pd.Series(np.sqrt(np.add(width, height)))
    dfpoke = pd.DataFrame({'distance': distance, 'pokemon': label})
    pichu = 0
    pikachu = 0
    iterations = 0
    proximity = 10
    dfpoke = dfpoke.sort_values("distance")

    for index in dfpoke.index:
        if dfpoke["pokemon"][index] == 1:
            pikachu += 1
        else:
            pichu += 1
        iterations += 1
        if iterations == proximity:
            break

    return True if pikachu >= pichu else False

print("Insert dimensions for pokemon calculated for 10 closest neighbor(violette dot):")
inpx, inpy = inputs()

if edistance10(inpx, inpy, df["width (cm)"], df["height (cm)"], df["(0-pichu 1-pikachu)"]):
    print("IT IS A PIKACHU")
    predict10 = "Pikachu"
else:
    print("IT IS A PICHU")
    predict10 = "Pichu"

plt.scatter(inpx, inpy, c = "purple")

plt.legend(["Pikachu","Pichu", "Testpoints: Pikachus", "Testpoints: Pichus",f"First Prediction 1 Neighbor({predict1})",f"Second Prediction 10 Neighbors({predict10})"])

plt.show()