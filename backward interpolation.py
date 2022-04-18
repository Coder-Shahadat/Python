def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u + i)
    return temp


def fact(n):
    f = 1
    for j in range(1, n + 1):
        f *= j
    return f


n = 8
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 1
y[1][0] = 8
y[2][0] = 27
y[3][0] = 64
y[4][0] = 125
y[5][0] = 216
y[6][0] = 343
y[7][0] = 512

for i in range(1,n):
    for j in range(n-1, i-1, -1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

for i in range(n):
    print(x[i], end='\t')
    for j in range(i + 1):
        print("{:4d}".format(y[i][j]), end='\t')
    print('')

value = 7.5
u = ((value - x[n - 1]) / (x[1] - x[0]))
sum = y[n - 1][0]
for i in range(1, n):
    sum += (u_cal(u, i) * y[n - 1][i]) / fact(i)
print("f({:.2f})".format(value), "=", sum)
