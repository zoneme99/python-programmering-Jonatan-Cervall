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
    x : x value on x-axis
    
    Returns
    -------
    Value of function of specific x Value

    round_ints
    --------
    rounds if func value (dydx) has atleast
    4 zeroes or 4 nines in it's first 4 decimals
    rounds up with 4 nines and rounds down if 4 zeroes
    """
    h = 1e-5
    dydx = ((func(x+h) - func(x)) / h)

    def round_ints(dydx):
        count = 0
        first = None
        for char in str(dydx).split(".")[-1]:
            if char == '0' or char == '9':
                if first == None:
                    first = char
                elif first != char:
                    break    
                count += 1
            else:
                break
        if not count < 4 and first == '0':
            return int(dydx)
        elif not count < 4 and first == '9':
            return int(dydx)+1
        else:
            return dydx
 
    return round_ints(dydx)
    
def func(x):
    return math.pow(x, 2)

def main():
    x = np.arange(1,10)
    data = [derivative_func(func, dx) for dx in x]
    print(data)
main()