n = int(input("n = "))
mina = int(input("a = "))
for i in range(1, n):
    a = float(input("a = "))
    if a % 2 != 0:
        if mina > a:
            mina = a
print("min = ", mina)

non_stop = input()
