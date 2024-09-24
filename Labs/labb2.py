import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("Labs/datapoints.csv")
print(df)

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

def distance(x,y, dataframe):
    tempdf = np.sqrt(np.pow(x,2) - np.pow(dataframe["width (cm)"]), 2) + np.pow(y,2) - np.pow(dataframe["height (cm)"],2)
    return tempdf
    
func = np.vectorize(distance)
print(func(finedata[0], df))


plt.show()