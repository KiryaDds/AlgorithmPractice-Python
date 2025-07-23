from math import factorial
y = 3
n = int(input("n = "))

for i in range(2, n + 1):
    y = y * (2 + (1 / factorial(i)))
print(y)

input()
