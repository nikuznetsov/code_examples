'''
RuCode-2020

Write a program, which calculates the last non-zero digit of the sum of k-x powers from the given values n and k
factorials of all integers in the range from 0 to n

Standart input: the first line contains two integers — a positive number n that does not exceed 100, and 
a non-negative number k that does not exceed 3
Standart output: print a single number — the last non-zero digit of the sum of k-th powers of factorials of integers 
from 0 to n inclusive
'''

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
