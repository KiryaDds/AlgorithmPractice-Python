from cmath import sqrt
choose = str(input("Оберіть приклад, розв'язки якого потрібно знайти (а, б): "))
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))


if choose == 'а':
    eps = 1e-8
    if abs(a) > eps:
        D = b**2 - 4*a*c
        if D < 0:
            print('\033[33mДійсних коренів немає')
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            print("Комплексні розв'язки: {}, {}".format(x1, x2))
        elif abs(D) < eps:
            x1 = -b / (2*a)
            print("x1 = x2 = {}".format(x1))
        else:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            print("Дійсні розв'язки: {}, {}".format(x1, x2))

    else:
        if abs(b) > eps:
            x1 = -c / b
            print("Єдиний розв'язок:", x1)
        else:
            if abs(c) > 0:
                print("Розв'язків немає")
            else:
                print("Нескінченна кількість розв'язків.")


elif choose == 'б':
    from math import sqrt
    D = b ** 2 - 4 * a * c

    if a != 0:                              # Якщо навпаки, то можна отримати помилку при розрахунку дискримінанта
        if D < 0:
            print("\033[33mДійсних розв'язків немає")

        elif D > 0:
            t1 = (-b + sqrt(D)) / (a * 2)  # Заміна: x^2 = t
            t2 = (-b - sqrt(D)) / (a * 2)
            if t1 >= 0:                     # x^2 !< 0
                x1 = sqrt(t1)
                print("\033[032mx1 = ", x1)
            if t2 >= 0:
                x2 = sqrt(t2)
                print("\033[035mx2 = ", x2)
            elif t1 < 0 and t2 < 0:
                print("\033[33mДійсних розв'язків немає")

        elif D == 0:
            t1 = -b / (a*2)
            if t1 >= 0:
                x1 = sqrt(t1)
                print("\033[032mx = ", x1)
            else:
                print("\033[33mДійсних розв'язків немає")

    else:
        if b != 0:                              # Цей параметр є знаменником у виразі -(c/b)
            if -(c / b) >= 0:                   # З цього виразу буде добуватися квадратний корінь
                x1 = -sqrt(-(c / b))
                x2 = sqrt(-(c / b))
                print("\033[032mx1 = ", x1)
                print("\033[035mx2 = ", x2)
            else:
                print("\033[33mДійсних розв'язків немає")
        else:
            print("Рівняння має безліч розв'язків")
else:
    print("\033[034mВи не обрали приклад")

non_stop = input()                              # Щоб консоль не закривалася
