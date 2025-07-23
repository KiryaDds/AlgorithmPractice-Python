import math

y = math.sqrt(2)
n = int(input("Визначте кількість коренів 'n': "))
for i in range(1, n):
    y = math.sqrt(y + 2)
print("y = ", y)

non_stop = input()
