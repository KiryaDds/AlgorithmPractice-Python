from math import sqrt
n = int(input("n = "))

for a in range(1, int(n)):
    for b in range(a, int(n)):
        m = a**2 + b**2
        c = int(sqrt(m))
        if m == c**2 and c <= n:
            print("{}^2 + {}^2 = {}^2".format(a, b, c))
non_stop = input()
