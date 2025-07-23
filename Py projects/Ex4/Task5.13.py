m = int(input("m = "))
n = int(input("n = "))
if n > 0 and m > 0 and n != 0:
    k = m / n
    for i in range(1, m):
        for j in range(1, n):
            if m % i == 0:
                p = i
                if n % j == 0:
                    q = j
                    for t in range(1, m + 1):
                        if k % (p / q) == 0 and (p / q == k * t):
                            if (k >= 1 and k >= p / q > 1) or (k <= 1 and k <= p / q < 1):
                                print("p = {}, q = {}".format(p, q))
else:
    print("Введіть натуральні числа!")
# if k % (p / q) == 0 -- p, q повинні бути натуральними.
input()
