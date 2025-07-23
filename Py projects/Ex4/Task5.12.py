n = int(input("n = "))
m = int(input("m = "))

if n < m:
    n, m = m, n

a, b = n, m
while m != 0:
    while n >= m:
        n -= m
    n, m = m, n % m
    print("n = {}, m = {}".format(n, m))
print("NSK = ", a * b / n)
non_stop = input()
