# Завдання 11.4 by  Янголь Ярослав / Комп. мех / 2 курс


def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = int(n // 2)
    x1 = int(x // 10**(half))
    x0 = int(x % 10**(half))
    y1 = int(y // 10**(half))
    y0 = int(y % 10**(half))

    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba(x0, y1) + karatsuba(x1, y0)
    z = z2 * 10**n + z1 * 10**half + z0
    return z


if __name__ == "__main__":

    a, b = map(int, input().split())
    print(karatsuba(a, b))