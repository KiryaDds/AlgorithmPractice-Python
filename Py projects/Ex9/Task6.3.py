squares = []
degrees = []
primes = []


def full_square(an):
    from math import sqrt
    if sqrt(an) == int(sqrt(an)):
        squares.append(an)


def five_degree(an):
    flag = 1
    if an % 5 == 0 and an % 10 != 0:
        a_mem = an
        while an != 5:
            if an % 5 == 0:
                an = an / 5
            else:
                flag = 0
                break
        if flag == 1:
            degrees.append(a_mem)


def is_prime(an):
    if an != 1:
        flag = 1
        if an == 2 or an == 3:
            primes.append(an)
        else:
            for j in range(2, an - 1):
                if an % j == 0:
                    flag = 0
                    break
            if flag == 1:
                primes.append(an)


n = int(input("n = "))
for i in range(1, n + 1):
    a = int(input("Введіть число послідовності: "))
    full_square(a)
    five_degree(a)
    is_prime(a)

print("Повними квадратами є: ", squares, ".")
print("Степенями п'ятірки є: ", degrees, ".")
print("Простими числами є: ", primes, ".")
