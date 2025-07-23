from math import sin
x = float(input("Введіть значення х: "))
n = int(input("Визначте кількість ітерацій: "))
y = sin(x)
i = 0
for i in range(n):
    y = sin(y)
print("y = ", y)
non_stop = input()
