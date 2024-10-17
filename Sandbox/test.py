import context
import function_class_saves.functions as fu
import matplotlib.pyplot as plt

start = 2
denom = 50

arr = [1/x for x in range(start,denom)]
def dec_replace(num):
    if str(num).split(".")[-1] == '0':
        return int(num)
    else:
        return num
arr = map(dec_replace, arr)
arr2 = [len(str(x).split(".")[-1]) if isinstance(x, float) else "" for x in arr]
x = [x for x in range(start,denom)]


plt.plot(x,arr2)
plt.show()