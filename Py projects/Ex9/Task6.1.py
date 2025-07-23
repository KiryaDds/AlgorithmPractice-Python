def f1(k):
    s = 0
    for i in range(1, k+2):
        s += 1.0/(k**2 + i)

    return s


n = int(input("n = "))
dob = 1
for i in range(n + 1):
    dob *= f1(i)
print("F({}) = {}".format(n, dob))
