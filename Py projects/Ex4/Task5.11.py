n = int(input("n = "))
m = int(input("m = "))

if n < m:
    n, m = m, n

while m != 0:
    while n >= m:
        n -= m
    n, m = m, n
    print("n = {}, m = {}".format(n, m))
print("NSD = ", n)
non_stop = input()
