n = int(input("n = "))
p = 1
if n < 0:
    print("\033[31mНе визначено!")
else:
    i = 1
    p = 1
    while i <= n:
        p *= i
        i += 1
print("{}!={}".format(n, p))
