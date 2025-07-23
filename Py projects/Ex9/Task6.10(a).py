from math import factorial


def sin_with_teilor(x):
    eps = 0.0001
    s = 0
    n = 0
    while eps < abs(x**(2*n-1)/factorial(n)):
        s += (-1)**n * (x**(2*n + 1))/factorial(2*n + 1)
        n += 1

    return s


x = float(input("x = (у радіанах): "))
print("sin({}) = {}".format(x, sin_with_teilor(x)))
