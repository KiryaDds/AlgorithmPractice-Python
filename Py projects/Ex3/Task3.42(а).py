n = int(input("n = "))
maxa = float(input("Введіть перше число: "))
count = 1
while n > 1:
    a = float(input("Введіть наступне число:"))
    if maxa < a:
        maxa = a
        n -= 1
    print(maxa)

non_stop = input()
