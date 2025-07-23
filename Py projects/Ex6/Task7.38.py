def input_poly():
    n = int(input("n = "))
    p = [0 for _ in range(n)]
    for i in range(0, n):
        p[i] = float(input("p[{}] = ".format(i)))
    return p


def values(p, x):
    v = 0
    for i in range(len(p)):
        v += x**i * p[i]
    return v


def derivat(p):
    res = [0 for _ in range(len(p) - 1)]
    for i in range(len(p) - 2, 0, -1):
        res[i] = (i + 1) * p[i + 1]
    return res


p = input_poly()
x = float(input("x = "))
print(values(derivat(p), x))
