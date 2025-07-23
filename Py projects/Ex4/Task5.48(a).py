n = int(input("n = "))
x1 = float(input("x[{}] = ".format(1)))
x2 = float(input("x[{}] = ".format(2)))
res = 1
for i in range(2, n):
    x3 = float(input("x[{}] = ".format(i + 1)))
    tmp = x1 + 2 * x2 + x3
    x1, x2 = x2, x3
    res *= tmp
print("p = {}".format(res))
non_stop = input()
