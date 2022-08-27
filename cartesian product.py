# https://github.com/Coder-Shahadat/Python/blob/main/cartesian%20product.py
from itertools import product

s = list(map(int, input().split()))

res = [(i, j) for i, j in product(s, repeat=2) if i % j == 0]
res2 = [(i, j) for i, j in product(s, repeat=2) if i <= j]

print("The pair order a/b : " + str(res))
print("The pair order a<=>b : " + str(res2))
