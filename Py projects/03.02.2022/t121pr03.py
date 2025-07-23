#  t121pr03.py
# -*- coding: cp1251 -*-

import os


def delspace(s):
    '''��������� ����� �������� �� �������.

    '''

    s = " ".join(s.split())

    return s


def formstr(L):
    '''������������ ������ L � �����.

    '''
    return L[0] + ";" + L[1] + ";" + ("%g" % L[2]) + (";%d" % L[3]) + (";%d;" % L[4]) + L[5] + "\n"


def linetxt(line):
    '''����������� ����� line � ����� ����� ������� ��.

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
    '''���������� ����� �� �� ����������.

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
    '''����� ����� ������ P1 �� ����� ������ P2.

    '''
    global in_f, new_f
    P1 = input('"�����" ������=')
    P1 = delspace(P1)
    P2 = input('" ����" ������=')
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
    '''���� ��� ��������� ������ �� S ���.

    '''
    global in_f, new_f
    S = int(input('������� ������ �������� ��='))
    f = open(in_f)
    nf = open(new_f, 'w')

    lines = f.readlines()
    for line in lines:
        l = line.split(';')
        new_wage = int(l[3]) + S
        line_updated = l[0] + ";" + l[1] + ";" + l[2] + ";" + str(new_wage) + ";" + str(new_wage * float(l[2])) + ";" + l[5]
        nf.write(line_updated)
    print("������ �����!")

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc4():
    '''����� ϲ� ���������� P1 �� ϲ� ���������� P2.

    '''
    global in_f, new_f
    P1 = input('"������" ϲ�=')
    P1 = delspace(P1)
    P2 = input('" �����" ϲ�=')
    P2 = delspace(P2)
    f = open(in_f)
    nf = open(new_f, 'w')

    lines = f.readlines()
    for line in lines:
        nf.write(line.replace(P1, P2))
    print("����� ϲ� ������!")

    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc5():
    '''���������� ����� (��������� ������ �� �� ���� ��������).

    '''
    global in_f, new_f
    K = input('��� ��������=')
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
    '''����������� (����|��������� ������ ������ �� �� ���� ��������).

    '''
    global in_f, new_f
    Ln = input('����� �� (���� �������� �������� ";"=\n')
    Ln = linetxt(Ln)
    Yes = True
    f = open(in_f)
    nf = open(new_f, 'w')

    K = input("������ ��� ��������, ���� ����� ������ ��� �������� ���� ������ ��� ��������� ������: ")
    lines = f.readlines()
    if K != "":
        Yes = False
        for line in lines:
            l = line.split(";")
            if l[0] == K:
                nf.write(line.replace(line, formstr(Ln)))
            else:
                nf.write(line)

    if Yes:  # ��������� ������ ������ ��
        for line in lines:
            nf.write(line)
        nf.write(formstr(Ln))
        
    f.close()
    nf.close()
    os.system("copy " + new_f + " " + in_f)
    os.remove(new_f)


def proc7():
    '''���� �������� �������.

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
    print("�������  ������".center(n))
    e = "=" * n
    print(e)
    print("���".center(Lc0), "������".center(Lc1), "ʳ���", " ���������", " ̳������ ", "ϲ� ����������".center(Lc5))
    print("��������".center(Lc0), " ".center(Lc1), "��.��", "�����(���)", " ��� (���)", " ".center(Lc5))
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
    '''���������� ����.

    '''

    Mn = ((1, "���������� ����� �� �� ����������"),
          (2, "����� ����� ������ P1 �� ����� ������ P2"),
          (3, "���� ��� ��������� ������ �� S ���"),
          (4, "����� ϲ� ���������� FIO1 �� ϲ� ���������� FIO2"),
          (5, "���������� ����� (��������� ������ �� �� ���� ��������)"),
          (6, "����������� (����|��������� ������ ������ �� �� ���� ��������)"),
          (7, "���� �������� �������"),
          (8, "ʳ���� ������"))
    LMn = len(Mn)

    while True:
        print("\n������ ������� �� :")  # ����'������� ����
        for i in range(LMn):
            print(Mn[i][0], "-", Mn[i][1])

        i = int(input("N="))
        if i == LMn:
            break
        elif i == 1:
            print("̳������ ��� �� �� ����������=%d" % proc1())
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
    