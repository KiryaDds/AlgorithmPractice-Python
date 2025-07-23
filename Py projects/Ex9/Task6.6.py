def heron(x, k, eps=0.0001):
    y0 = 1.0
    y1 = y0 + (x / y0**(k - 1) - y0) / k

    return (y1 + y0) / 2.0


def task6_6(a, e=0.0001):
    return heron(a, 3, eps=e) - heron(a**2 + 1, 6, eps=e)/(1 + heron(a + 3, 7, eps=e))


x = float(input("x = "))
print("y = ", task6_6(x))
