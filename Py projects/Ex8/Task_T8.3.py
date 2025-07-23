karta = {}

n = int(input("n = "))
for i in range(n):
    row = input("Row {}:".format(i))    # 4, 5, 3, 000011111000
    sp = map(int, row.split(", "))
    even = True
    j = 0
    for x in sp:
        if even:
            for k in range(j, j + x):
                karta[(i, k)] = 0
        else:
            for k in range(j, j + x):
                karta[(i, k)] = 1
        j += x
        even = not even

print(karta)
