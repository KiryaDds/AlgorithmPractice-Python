import math

n = int(input("Визначте кількість коренів 'n': "))

y = math.sqrt(3 * n)

for k in range(1, n):
    y = math.sqrt(y + 3 * (n - k))
print("y = ", y)
