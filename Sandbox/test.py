

import pandas as pd
import numpy as np

x = pd.Series(np.array([15,5,30]), index = [x for x in range(3)])
x = x.argmin()
print(x)

index = list()
df = pd.read_csv("Labs/datapoints.csv")

width = df["width (cm)"]
index.append(width.argmin())
width = width.drop(width.argmin(), axis=0)
index.append(width.argmin())
print(index)

