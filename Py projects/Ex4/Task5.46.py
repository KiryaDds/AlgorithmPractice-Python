x = float(input("x = "))
y = float(input("y = "))

if x <= 0 and y <= 1:
    print("Не задовільняє умову!")
else:
    k = int(0)
    if y**(k - 1) <= x < y**k:
        print("k = ", k)
    else:

        i = 0
        while True:
            if y**(i - 1) <= x < y**i:
                k = i
                print("k = ", k)
            elif i == 100:
                print("Додатніх k не знайдено!")
                break
            i += 1

        j = 0
        while True:
            if y**(j - 1) <= x < y**j:
                k = j
                print("k = ", k)
            elif j == 100:
                print("Від'ємних k не знайдено!")
                break
            j += 1

input()
