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


def derive_function(func):
    """
    Derive a function and return the derived function
    
    Parameters
    ----------
    func : function
        The function to be derived
    
    Returns
    -------
    derived_func : function
        The derived function
    """
    def derived_func(x):
        h = 1e-8
        return (func(x+h) - func(x-h)) / (2*h)
    return derived_func
    
def func(x):
    return math.pow(x, 3)


func = derive_function(func)

print(func(2))
print(1e-1)