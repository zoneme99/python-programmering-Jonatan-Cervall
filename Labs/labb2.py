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

def term(testpoint, testx):
    res = np.pow(testpoint - testx,2)
    return res  

ndf = pd.DataFrame
ndf["x"] = df["width (cm)"].map(term,finedata[0])
print(ndf["x"])
#gör en copy av df och elementvis subtrahera och kvadrera värderna. Därefter addera och ta roten ur på copy df


#dist = list(map(distance, df, finedata[0], finedata[1]))
#print(dist)

plt.show()