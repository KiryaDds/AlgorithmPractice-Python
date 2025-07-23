n = int(input("Визначте кількість членів 'n': "))
x = int(input("Визначте 'x': "))
y = n * x**(n - 1)
for i in range(1, n):
    y += (n - i) * x**(n - 1 - i)
print("y = ", y)

non_stop = input()
