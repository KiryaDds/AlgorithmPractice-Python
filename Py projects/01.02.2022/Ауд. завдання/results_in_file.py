# Виконує запис інформації у окремий файл згідно умов 2-го завдання.
# Результат є в файлі "2 завдання.txt" або отримується при виконанні цього файлу.

from struct import pack, unpack


def exist_tria(a, b, c):
    '''? Чи є трикутник при значеннях чисел a,b,c.

    '''
    f = a > 0 and b > 0 and c > 0
    return f and a + b > c and b + c > a and c + a > b

def per(a, b, c):
    '''Периметр трикутника зі сторонами a,b,c.

    '''
    return a + b + c

def area(a, b, c):
    '''Площа трикутника зі сторонами a,b,c.

    '''
    p = 0.5 * per(a, b, c)
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def get_txt(namef_in, Type, namef_out):
    '''Читання і обробка текстового файлу з числами типу Type.

       namef_in - повне ім'я вхідного файла на зовнішньому носії;
       Type  - тип чисел;
       namef_out - повне ім'я вихідного файла на зовнішньому носії.
    '''
    fi = open(namef_in); fo = open(namef_out, 'w')
    for L in fi:
        if len(L) > 0:
            L = L.split()
            if len(L) > 2:
                for i in range(3):
                    L[i] = Type(L[i])
                L = L[0:3]
                if exist_tria(*L) :
                    P = per(*L)
                    S = area(*L)
                    fo.write("%g %g %g %f %e\n" % (L[0], L[1], L[2], P, S))
    fi.close(); fo.close()

def get_txt_to_bin(namef_in, Type, namef_out):
    '''Читання і обробка текстового файлу з числами типу Type.

       namef_in - повне ім'я вхідного файла на зовнішньому носії;
       Type  - тип чисел;
       namef_out - повне ім'я вихідного бінарного файла на зовнішньому носії.
    '''
    fi = open(namef_in)
    fo = open(namef_out, 'wb')  # бінарний файл для запису
    fmt = "d"*5                 # формат для запису 5-ти дійсних чисел (double)
    for L in fi:
        if len(L) > 0:
            L = L.split()
            if len(L) > 2:
                for i in range(3):
                    L[i] = Type(L[i])
                L = L[0:3]
                if exist_tria(*L) :
                    P = per(*L)
                    S = area(*L)
                    fo.write(pack(fmt, L[0], L[1], L[2], P, S))
                    fo.flush()
    fi.close(); fo.close()






def print_txtf(namef, result_f):
    s1 = "    Ім'я файлу = " + namef
    f = open(namef); rf = open(result_f, "a"); rf.write("\n"); rf.write(s1); rf.write("    \n")
    while True :
        L = f.readline()
        if len(L) == 0: break
        s = L + " "
        rf.write(s)
    rf.write("\n")
    rf.write("\n")
    f.close()


def print_binf(namef, nb, fmt, result_f):
    s1 = "    Ім'я файлу = " + namef
    f = open(namef,"rb"); rf = open(result_f, "a"); rf.write("\n"); rf.write(s1); rf.write("    \n")
    s = f.read(nb)              # читання nb байт
    while s :
        x = unpack(fmt, s)
        s = ""
        for e in x:
            s += "%13.5g " % e
        s += "\n"
        rf.write(s)
        s = f.read(nb)
    rf.write("\n")
    rf.write("\n")
    f.close()


if __name__ == "__main__" :
    in_f = input("Введіть повне ім'я вхідного txt-файлу на зовнішньому носії :\n")
    res_f = input("Введіть повне ім'я \033[031mрезультативного\033[039m txt-файлу на зовнішньому носії :\n")
    rf = open(res_f, "w")

    print("  a) :")
    out_f = input("Введіть повне ім'я вихідного txt-файлу на зовнішньому носії :\n")

    print_txtf(in_f, res_f)

    get_txt(in_f, float, out_f)

    print_txtf(out_f, res_f)

    print("  b) :")
    out_f = input("Введіть повне ім'я вихідного bin-файлу на зовнішньому носії :\n")

    print_txtf(in_f, res_f)

    get_txt_to_bin(in_f, float, out_f)

    print_binf(out_f, 40, "d"*5, res_f)
    rf.close()

