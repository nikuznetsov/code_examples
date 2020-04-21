import math

nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
s = 0
if (n <= 100) and (k <= 3) and (k >= 0) and (n >= 0):
    for i in range(n+1):
        s += (math.factorial(i))**k
    for i in (str(s)[::-1]):
        if i != '0':
            print(i)
            break