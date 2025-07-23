def input_vector():
    n = int(input("n = "))
    vect = []
    for i in range(n):
        x = float(input("x[{}] = ".format(i)))
        vect.append(x)
    return vect


def more_amount(vect):
    amount = 0
    a = float(input("Введіть число, з яким будемо порівнювати компоненти вектора: "))
    for i in range(0, len(vect)):
        if i > a:
            amount += 1
    return amount


v = input_vector()
more_amount(v)
