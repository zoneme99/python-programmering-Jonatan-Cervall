# import numpy as np

# array = ['1.2','2.0','3.2']
# f = np.vectorize(float)
# print(f(array))

# from collections import Counter
# b = [2,2,2,2,2,5,5,4,4,6,6,1,1,8,8,9,7]
# a = Counter(b)
# a = sorted(a)
# print(a)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = np.multiply(np.multiply(2,np.log(x)), np.pow(x, 2)) 
plt.plot(x,y)
plt.show()