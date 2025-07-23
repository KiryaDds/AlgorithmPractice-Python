def input_vector():
    n = int(input("Довжина n = "))
    vect = []
    for i in range(n):
        x = float(input("x[{}] = ".format(i)))
        vect.append(x)
    return vect


def vect_move_cycle(v, k):
    while k != 0:
        v1 = v[0]
        for i in range(len(v)):
            if i == len(v) - 1:
                v[i] = v1
            else:
                v[i] = v[i + 1]
        k -= 1
    return v


print("Введіть ветктор: ")
v = input_vector()
print(v)
print()
k = int(input("Введіть кількість циклів зсуву вектора: "))
print(vect_move_cycle(v, k))
