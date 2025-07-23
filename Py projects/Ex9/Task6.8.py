def graf(x):
    m = int((x - 0.25)/0.5)
    y = x - 0.5*m - 0.25
    if m % 2 == 0:
        return 0.25 - y
    else:
        return y - 0.25


x = float(input("x = "))
print("f({}) = {}".format(x, graf(x)))
