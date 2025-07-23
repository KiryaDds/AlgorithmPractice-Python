#  t121pr03.py
# -*- coding: cp1251 -*-

import os


def delspace(s):
    '''Видалення лишніх пропусків між словами.

    '''

    s = " ".join(s.split())

    return s


def formstr(L):
    '''Перетворення запису L в рядок.

    '''
    return L[0] + ";" + L[1] + ";" + ("%g" % L[2]) + (";%d" % L[3]) + (";%d;" % L[4]) + L[5] + "\n"


def linetxt(line):
    '''Переворення рядка line в запис рядка таблиці ШР.

    '''
    lst = line.split(';')
    lst[0] = lst[0].strip()
    lst[1] = delspace(lst[1])
    lst[2] = float(lst[2])
    lst[3] = int(lst[3])
    lst[4] = float(lst[4])
    lst[5] = delspace(lst[5])
    return lst


def proc1():
    '''Обчислення фонду ЗП по організації.

    '''
    global in_f
    f = open(in_f)

    S = 0
    lines = f.readlines()
    for line in lines:
        l = line.split(";")
        if len(l) > 4:
            S += int(l[4])

    f.close()
    return S


def proc2():
    '''Заміна назви посади P1 на назву посади P2.

    '''
    global in_f, new_f
    P1 = input('"стара" посада=')
    P1 = delspace(P1)
    P2 = input('" нова" посада=')
    P2 = delspace(P2)
    f = open(in_f)
    nf = open(new_f, 'w')

    print(P1)
    print(P2)

    lines = f.readlines()
    for line in lines:
        nf.write(line.replace(P1, P2))

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc3():
    '''Зміна всіх посадових окладів на S грн.

    '''
    global in_f, new_f
    S = int(input('Посадові оклади збільшити на='))
    f = open(in_f)
    nf = open(new_f, 'w')

    lines = f.readlines()
    for line in lines:
        l = line.split(';')
        new_wage = int(l[3]) + S
        line_updated = l[0] + ";" + l[1] + ";" + l[2] + ";" + str(new_wage) + ";" + str(new_wage * float(l[2])) + ";" + l[5]
        nf.write(line_updated)
    print("Оклади змінені!")

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc4():
    '''Заміна ПІБ працівника P1 на ПІБ працівника P2.

    '''
    global in_f, new_f
    P1 = input('"старий" ПІБ=')
    P1 = delspace(P1)
    P2 = input('" новий" ПІБ=')
    P2 = delspace(P2)
    f = open(in_f)
    nf = open(new_f, 'w')

    lines = f.readlines()
    for line in lines:
        nf.write(line.replace(P1, P2))
    print("Заміна ПІБ успішна!")

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc5():
    '''Скорочення штату (видалення запису ШР по коду підрозділу).

    '''
    global in_f, new_f
    K = input('Код підрозділу=')
    K = K.strip()
    f = open(in_f)
    nf = open(new_f, 'w')

    lines = f.readlines()
    for line in lines:
        l = line.split(";")
        if l[0] == K:
            continue
        nf.write(line)

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc6():
    '''Редагування (зміна|додавання нового запису ШР по коду підрозділу).

    '''
    global in_f, new_f
    Ln = input('Запис ШР (поля розділять символом ";"=\n')
    Ln = linetxt(Ln)
    Yes = True
    f = open(in_f)
    nf = open(new_f, 'w')

    K = input("Введіть код підрозділу, який треба змінити або зоставте поле пустим для додавання нового: ")
    lines = f.readlines()
    if K != "":
        Yes = False
        for line in lines:
            l = line.split(";")
            if l[0] == K:
                nf.write(line.replace(line, formstr(Ln)))
            else:
                nf.write(line)

    if Yes:  # додавання нового запису ШР
        for line in lines:
            nf.write(line)
        nf.write(formstr(Ln))
        
    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc7():
    '''Друк штатного розпису.

    '''
    global in_f, new_f
    f = open(in_f)
    lstL = []
    Lc0 = 10
    Lc1 = 0
    Lc5 = 14
    for line in f:
        L = linetxt(line)
        lstL.append(L)
        e = len(L[0])
        if Lc0 < e: Lc0 = e
        e = len(L[1])
        if Lc1 < e: Lc1 = e
        e = len(L[5])
        if Lc5 < e: Lc5 = e
    f.close()
    n = 5 + Lc0 + Lc1 + Lc5 + 5 + 10 + 10
    print()
    print("ШТАТНИЙ  РОЗПИС".center(n))
    e = "=" * n
    print(e)
    print("Код".center(Lc0), "Посада".center(Lc1), "Кільк", " Посадовий", " Місячний ", "ПІБ Працівника".center(Lc5))
    print("підрозділу".center(Lc0), " ".center(Lc1), "Шт.Од", "Оклад(грн)", " ФЗП (грн)", " ".center(Lc5))
    print(e)
    lstL.sort()
    nf = open(new_f, 'w')
    for L in lstL:
        print(L[0].ljust(Lc0), L[1].ljust(Lc1), "%5g" % L[2], "%10d" % L[3], "%10d" % L[4], L[5].ljust(Lc5))
        nf.write(formstr(L))
    print("-" * n + "\n")

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def menu():
    '''Організація меню.

    '''

    Mn = ((1, "Обчислення фонду ЗП по організації"),
          (2, "Заміна назви посади P1 на назву посади P2"),
          (3, "Зміна всіх посадових окладів на S грн"),
          (4, "Заміна ПІБ працівника FIO1 на ПІБ працівника FIO2"),
          (5, "Скорочення штату (видалення запису ШР по коду підрозділу)"),
          (6, "Редагування (зміна|додавання нового запису ШР по коду підрозділу)"),
          (7, "Друк штатного розпису"),
          (8, "Кінець роботи"))
    LMn = len(Mn)

    while True:
        print("\nОберіть потрібну дію :")  # Пред'явлення меню
        for i in range(LMn):
            print(Mn[i][0], "-", Mn[i][1])

        i = int(input("N="))
        if i == LMn:
            break
        elif i == 1:
            print("Місячний ФОТ ЗП по організації=%d" % proc1())
        elif i == 2:
            proc2()
        elif i == 3:
            proc3()
        elif i == 4:
            proc4()
        elif i == 5:
            proc5()
        elif i == 6:
            proc6()
        elif i == 7:
            proc7()


if __name__ == '__main__':
    global in_f, new_f
    in_f = 'statrozp.csv'
    new_f = 'temp.csv'
    from t121pr01 import print_txtf

    print_txtf(in_f)
    menu()
    