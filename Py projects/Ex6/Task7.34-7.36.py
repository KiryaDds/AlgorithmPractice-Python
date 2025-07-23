def input_vector():
    n = int(input("n = "))
    vect = []
    for i in range(n):
        x = float(input("x[{}] = ".format(i)))
        vect.append(x)
    return vect


def output_vector(v):
    for x in v:
        print(x, end="")


'''
def outEven0(v):
    for i in range(len(v)):
        print("i = %d"%(i))
        if i % 2 == 0:
            print(v[i])
'''


def out_even1(v):
    for i in range(0, len(v), 2):
        print(v[i])


def out_positive(v):
    for x in v:
        if x > 0:
            print(x)


def avg_vector(v):
    if len(v) == 0:
        return None
    else:
        return sum(v)/len(v)


def norm_vector(v):
    from math import sqrt
    sum_sqr = 0
    for x in v:
        sum_sqr += x**2
    return sqrt(sum_sqr)


def dist(v1, v2):
    from math import sqrt
    if len(v1) != len(v2):
        return None
    n = len(v1)
    s = 0
    for i in range(n):
        s += (v1[i] - v2[i])**2
    return sqrt(s)


'''
def dist(v1, v2):
    from math import sqrt
    if len(v1) != len(v2):
        return None
    s = 0
    for x, y in zip(v1, v2):
        s += (x - y)**2
    return sqrt(s)
'''


v1 = input_vector()
print()
v2 = input_vector()
print()

print(v1)
print()
output_vector(v2)
print()

print()
print("Компоненти з парними номерами з першого введеного вектору: ")
out_even1(v1)

print()
print("Додатні компоненти з другого вектору: ")
out_positive(v2)

print()
print("Average = {], normal = {}.".format(avg_vector(v1), norm_vector(v1)))

print()
print("Dist = {}.".format(dist(v1, v2)))
