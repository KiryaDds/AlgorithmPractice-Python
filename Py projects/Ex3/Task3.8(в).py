n = int(input("Визначте кількість членів 'n': "))
x = int(input("Визначте 'x': "))
fact = 1
i = n
y = 1
while i > 1:
    fact *= i
    z = x**(i - 1) / fact
    y += z
    i -= i
print("y = ", y)

non_stop = input()
