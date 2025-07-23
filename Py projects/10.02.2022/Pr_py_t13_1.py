# Основний файл для виконання завдання
# Працює з пустими файлами та файлами з неповними наборами значень p та q

from Segm import Segm


def get_segm(p, q):
    """Функція знаходження відрізка розв'язку
       нерівності x^2 + px + q < 0
    """

    s = Segm()
    D = (p**2 - 4*q)**0.5
    x1 = (-p + D) / 2
    x2 = (-p - D) / 2
    if x1 > x2:
        s.set_Segm(x2, x1)
    else:
        s.set_Segm(x1, x2)

    return s


if __name__ == "__main__":
    sol = Segm()
    number = 1
    file_name = input("Введіть ім'я файлу або зоставте поле пустим \nдля використання файлу за замовчуванням: ")    # k12_t13_1.txt
    if file_name == "":
        file_name = "k12_t13_1.txt"
    print("\033[033mВикористано дані з файлу\033[036m '{}'\033[039m".format(file_name))
    print()
    f = open(file_name, "r")
    for line in f:
        line = line.replace(";", " ")
        line = line.replace(",", " ")
        if line == "" or line == "\n":
            continue

        line = line.split()
        if len(line) < 2:
            continue

        p = float(line[0])
        q = float(line[1])
        sl = get_segm(p, q)

        print(str(number) + " нерівність: x^2{}x{} < 0 її розв'язок = {}".format(p, q, sl))
        if sol.is_empty():
            sol = sl
        else:
            sol = sol.crossingSegm(sl)
        number += 1

    if sol.is_empty():
        print("\033[031mРозв'язків немає!\033[039m")
    else:
        print("\033[032mРозв'язок системи квадратних нерівностей: \033[039m", sol)
