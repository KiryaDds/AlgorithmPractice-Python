from math import *

x = float(input())

a0 = x / 2
EPS = 0.000001

while True:
    a1 = 0.5 * (a0 + x / a0)
    if abs(a1 - a0) < EPS:
        break
    a0 = a1

print((a1 + a0)/2.0, sqrt(x))

non_stop = input()
