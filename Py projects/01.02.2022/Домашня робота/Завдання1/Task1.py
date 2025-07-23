# Виконує 1 завдання з домашньої роботи. За замовчування використовує файл "vect.txt" на вхід
# та файл "out.txt" на вихід.


def get_list(fname):        # Вхідний файл у консоль + створення списку для 1 пункту
    f = open(fname)
    n = f.read(1)
    vectors = []
    for L in f:
        vectors.append(L.split())
    vectors.pop(0)
    print(vectors)
    return vectors, n


def is_ort_pair(v1, v2):       # Перевірка пари векторів на ортогональність
    mult = 0
    k = len(v1)
    for i in range(k):
        mult += int(v1[i]) * int(v2[i])
    if mult == 0:
        return True
    else:
        return False


def f_write(f_in, f_out):   # Запис у файл для 3 пункту
    f = open(f_in)
    s = "\nІм'я файлу: " + f_in + '\n'
    f_out.write(s)
    while True:
        s = f.readline()
        if len(s) == 0:
            break
        s += ""
        f_out.write(s.lstrip())
    f_out.write("")
    f.close()


def mini_set_creator(set, v):           # 2 пункт
    amount = len(set)
    f = True
    for i in range(amount):
        if not(is_ort_pair(set[i], v)):
            f = False
            break
    if f:
        set.append(v)
    return set


def sets_creator(v):
    sets = []
    amount = len(v)
    for i in range(amount):
        set = [v[i]]
        for j in range(amount):
            if i < j:
                set = mini_set_creator(set, v[j])
        if len(set) > 1:
            sets.append(set)
    return sets


if __name__ == "__main__":
    filename = input("Введіть ім'я вхідного файлу або залиште строку пустою для використання файла по замовчуванню:")
    if filename == "":
        filename = "vect.txt"

    out_filename = input("Введіть ім'я вихідного файлу або залиште строку пустою для створення файла з назвою 'out.txt':")
    if out_filename == "":
        out_filename = "out.txt"

    vectors, n = get_list(filename)

    ff = open(out_filename, "w")

    f_write(filename, ff)

    ff.write('\n')
    ff.write('\nВектори: ')
    ff.write('\n' + str(n))
    for i in vectors:
        ff.write('\n')
        ff.write(str(i))

    tt = sets_creator(vectors)
    ff.write('\n')
    ff.write('\nОртогональні вектори:')
    ff.write('\n' + str(n))
    for i in tt:
        ff.write('\n')
        ff.write(str(i))

    ff.close()
