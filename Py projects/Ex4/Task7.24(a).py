from math import *

z = float(input("z = "))
n = 1
e0 = 1
EPS = 0.0000001
while True:
    e = e0 + z**n / factorial(n)
    if abs(e - e0) < EPS:
        break
    n += 1
    e0 = e
print("Сума дорівнює: ", e)
input()
