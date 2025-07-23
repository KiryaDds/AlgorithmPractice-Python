#  t12_2a01.py
'''
1. Використовуючи модулі random, struct написати процедуру запису n
   псевдовипадкових дійсних чисел з діапазону [-1000, 1000] в
   бінарний файл прямого доступу (БФПД).
2. Написати процедуру друку елементів, записаних в БФПД.
3. Написати процедуру заміни кожного від'ємного елемента в БФПД на
   його квадрат.
Написати тестуючу програму.
'''

from struct import pack, unpack


def put_float_BFD(n, namef, diap=1000):
    '''Запис n псевдовипадкових дійсних чисел з діапазону [-diap, diap] в БФПД.

    '''
    import random
    f = open(namef, 'w+b')
    for k in range(n):
        x = random.uniform(-diap, diap)
        f.write(pack("d", x))
        f.flush()
    f.close()


def print_BFD(namef):
    '''Друк вмісту БФПД.

    '''
    print("Ім'я файлу=", namef, file=fpr)
    f = open(namef, 'r+b')
    s = f.read(8)
    i = 0
    while s:
        x = unpack("d", s)
        i += 1
        print("%13.8g" % x[0], end=' ', file=fpr)
        if i % 5 == 0: print(file=fpr)
        s = f.read(8)
    print(file=fpr)
    f.close()


def rw_BFD(namef):
    '''Читання і обробка БФПД.

    '''
    f = open(namef, 'r+b')
    s = f.read(8)
    while s:
        x = unpack("d", s)[0]
        if x < 0:
            x *= x
            f.seek(-8, 1)  # встановлення маркера перед прочитаним елементом
            f.write(pack("d", x))
            f.flush()
        s = f.read(8)
    f.close()


if __name__ == "__main__":
    n = int(input("? число елементів="))
    out_b = input("Введіть повне ім'я вихідного бінарного файлу=")
    prnt = input("Введіть повне ім'я вихідного текстового файлу для друку=")
    fpr = open(prnt, "w")
    put_float_BFD(n, out_b)
    print("== Створений ==", file=fpr)
    print_BFD(out_b)

    rw_BFD(out_b)
    print("== Після заміни ==", file=fpr)
    print_BFD(out_b)
    fpr.close()
