import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-100,100,100)
y = [y**2 for y in x]

plt.plot(x,y)
plt.show()