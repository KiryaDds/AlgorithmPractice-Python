r = float(input('r = '))
a = float(input('a = '))
b = float(input('b = '))
d = float(input('d = '))

r1 = (a**2 + b**2) < r**2
r2 = (a**2 + (b + d**2)**2) < r**2

print(r1, r2)

if not r1:
    if not r2:
        print("Відрізок усередені, точок перетину немає.")
    else:
        print("Одна точка перетину.")
elif r2:
    print("Одна точка перетину.")
else:
    print("Відрізок ззовні кола.")
    if (b * (b + d**2) < 0) and abs(a) < r:
        print("Дві точки перетину.")
    else:
        print("Точок перетину немає.")

non_stop = input()
