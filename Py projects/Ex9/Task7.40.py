def func(*xn, **yn):
    x = []
    for i in xn:
        x.append(i)

    print(x)

    y = []
    for j in yn.values():
        y.append(j)

    res = 1
    for a, b in zip(xn, yn):
        res *= a**3 + int(b)**3
    return res


print(func(1234, 43, 34, 1, 45, 234))
