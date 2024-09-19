import time
iter = 100000
lst = list()
st = ""
start_time = time.time()
for _ in range(iter):
    lst.append("a")
print(f"time append: {time.time()- start_time}")

start_time = time.time()
for _ in range(iter):
    st += "a"
print(f"time + operation: {time.time()- start_time}")