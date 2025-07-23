# a)
from math import sqrt


def task6_23a(x):
    if x < 8.1e-6:
        return 0
    else:
        return task6_23a(x/2) + sqrt(x)


print(task6_23a(1.0), task6_23a(2.0))


def task6_23b(x):
    if x < 0.1e-6 or x > 1000:
        return 0
    else:
        return task6_23b(x * 10) + 1/x


print(task6_23b(1.0), task6_23b(200.0))

# dopysaty