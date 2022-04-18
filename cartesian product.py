from itertools import product

with open("p1.txt") as g:
    s = list(map(int, g.readlines()))
print("S = " + str(s))

res = [(i, j) for i, j in product(s, repeat=2) if i % j == 0]
res2 = [(i, j) for i, j in product(s, repeat=2) if i <= j]

print("The pair order a/b : " + str(res))
print("The pair order a<=>b : " + str(res2))
