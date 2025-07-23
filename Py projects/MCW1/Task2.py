from math import inf
x = float(input("x = "))
eps = float(input("eps = "))
if x != 0 and abs(x) < 1 and eps > 0:
    y = 1 / 8
    k = 1
    j = True
    while j is True:
        while abs(y) >= eps:
            y += ((-1)**k * x**2 * k) / (k + 2)**3
            k += 1
        else:
            j = False
            break

    print(y)
