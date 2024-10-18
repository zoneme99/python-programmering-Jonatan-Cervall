import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# df = pd.read_csv('Sandbox/50000_Sales_Records.csv')
# group = df.groupby('Region')
# mean_by_region = group['Total Revenue'].mean()
# df = df.set_index('hej')
# print(df.head(5))

def derivative_func(func, x):
    """
    Derive a function with speicific x
    and return value
    
    Parameters
    ----------
    func : function
        The function to be derived
    
    Returns
    -------
    derived_func : function
        The derived function
    """
    h = 1e-10
    return ((func(x+h) - func(x)) / h) 
    
def func(x):
    return math.pow(x, 2)


x = [x for x in range(1,101)]

data = [derivative_func(func, dx) for dx in x]
print(data)
count = 0
counter = list()
for parse in data:
    for char in str(parse).split(".")[-1]:
        if char == '0' or char == '9':
            count += 1
        else:
            counter.append(count)
            count = 0
            break
print(counter)
