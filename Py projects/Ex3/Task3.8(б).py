n = int(input("Визначте 'n': "))
m = int(input("Визначте 'm': "))
x = int(input("Визначте 'x': "))
if n and m >= 0:
    y = x**n * (1 - x)**m
    print("y = ", y)
else:
    print("\033[31mn i m повинні буть невід'ємними!")

non_stop = input()
