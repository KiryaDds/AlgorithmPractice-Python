from math import sqrt
squares = []


def is_sqr(n):
    m = int(sqrt(n + 0.5))
    return m**2 == n


def is_sum_sqr(n):
    for i in range(0, n//2 + 1):
        if is_sqr(i) and is_sqr(n - i):
            return True
    return False


n = int(input("n = "))
for i in range(n):
    if is_sum_sqr(i):
        print(i)
