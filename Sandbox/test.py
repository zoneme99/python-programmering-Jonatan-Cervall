import random as rnd

lst = [rnd.randint(1,10) % rnd.randint(1,10) for _ in range(10)]
print(lst)