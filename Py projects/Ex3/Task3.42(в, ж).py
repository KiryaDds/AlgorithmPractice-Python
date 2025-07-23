n = int(input("n = "))
maxa = 0
for i in range(1, n + 1):
    a = float(input("a = "))
    if a % 2 == 0:
        if maxa < a:
            maxa = a
    if a % 2 != 0:
        if maxa < a * (-1):
            maxa = a
    print(maxa)

Non_stop = input()
