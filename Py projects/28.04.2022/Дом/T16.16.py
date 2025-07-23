# T16_16
# Номер варіанта 14


def fact(n):
    if n == 0: y = 1
    else: y = n * fact(n - 1)
    return y


def var14(x, eps=1e-8):
    """Функція для підрахунку суми всіх елементів послідовності

    """
    def GXn(x):
        """Генератор-функція"""
        n = 1; p = x*x/(4*n*n+2*n); a = -x; S = 0
        yield S, a
        while True:
            a *= p; S += a; n += 1
            yield S, a

    e = eps if 0 < eps < 1 else 1e-8
    for S, a in GXn(x):
        if abs(a) <= e: break
    return S


x = float(input("x = "))
print("var14(%g) = %17.10e \n" % (x, var14(x, 1e-5)))
