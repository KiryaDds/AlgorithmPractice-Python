from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    m = int(sqrt(n)) + 1
    for i in range(2, m):
        if n % i == 0:
            return False

    return True


# print(is_prime(7), is_prime(4), is_prime(45), is_prime(109), is_prime(121))

n = int(input("n = "))
for i in range(n, 2*n+1):
    if is_prime(i) and is_prime(i + 2) and i + 2 <= 2*n:
        print("Twins: ", i, i + 2)
