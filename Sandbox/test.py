

import pandas as pd
import numpy as np

x = pd.Series(np.array([15,5,30]), index = [x for x in range(3)])
y = pd.Series(np.array([20,10,40]), index = [x for x in range(3)])

df = pd.DataFrame({'Column1': x, 'Column2': y})
df = df.sort_values("Column2")
ff = pd.DataFrame()

print(df)
print(df.index)

 