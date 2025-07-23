n = int(input("n = "))
mina = int(input("a = "))
i = 1
a = mina
while i <= n:
    a = a * i
    i += 1
    if mina > a:
        mina = a
    print("min = ", mina)

non_stop = input()
