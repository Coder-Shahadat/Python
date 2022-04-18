from itertools import product
import numpy as np

a = [1, 2, 3]
b = [1, 2]

res = [(i, j) for i, j in product(a, b) if i > j]
res2 = [1 if i > j else 0 for i in a for j in b]
data = np.array(res2).reshape(3, 2)

print(res)
print(data)
