# import numpy as np

# array = ['1.2','2.0','3.2']
# f = np.vectorize(float)
# print(f(array))
from collections import Counter
b = [2,2,2,2,2,5,5,4,4,6,6,1,1,8,8,9,7]
a = Counter(b)
a = sorted(a)
print(a)