# Завдання 1

import pickle


def get_vectorslist_txt(f_in):
    vects = []
    f = open(f_in, "r")
    lines = f.readlines()
    for line in lines:
        line = line.split(';')
        for i in range((len(line))):

            vects.append(list(map(int, line[i].split())))

    return vects


def print_in(f_out, list_v):
    f = open(f_out, "bw")
    pickle.dump(list_v, f)
    f.flush()
    f.close()


def get_vectorlist_bin(f_in):
    f_in = open(f_in, 'br')
    vects = pickle.load(f_in)
    f_in.close()

    return vects


if __name__ == "__main__":
    file_in = input("Введіть повне ім'я вхідного txt-файлу або зоставте поле пустим для використання файлу \n"
                    "'default.txt' за замовчуванням: ")
    file_out = input("Введіть повне ім'я вихідного bin-файлу або зоставте поле пустим для створеня файлу \n"
                     "'binary_vectors_by_pickle.bin' за замовчуванням: ")
    if file_in == "":
        file_in = "default.txt"
    if file_out == "":
        file_out = "binary_vectors_by_pickle.bin"
    print()

    vect_list = get_vectorslist_txt(file_in)
    print("Список векторів із txt-файлу: ", vect_list)
    print()

    print_in(file_out, vect_list)
    print("\033[034mБінарний файл записано!\033[039m")
    print()

    vects_from_bin = get_vectorlist_bin(file_out)
    print("\033[033mСписок векторів із бінарного файлу:\033[039m ", vects_from_bin)
    print()
    print()
    if vect_list == vects_from_bin:
        print("\033[032mТестування виконано вдало!\033[039m")

