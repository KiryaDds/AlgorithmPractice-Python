# Цей файл виконує 2 завдання


def get_sortedfile(fname1, fname2):
    f1 = open(fname1)
    f2 = open(fname2)
    info1 = f1.readlines()
    info2 = f2.readlines()

    all_lines = ""
    for i in info1:
        all_lines += " " + i
    for i in info2:
        all_lines += " " + i

    all_lines = all_lines.replace("\n", "")
    s = list(map(int, all_lines.split()))
    fname = "file_merj.txt"
    f = open(fname, "w")
    for j in s:
        f.write(str(j) + "\n")
    f.close()


get_sortedfile("file1.txt", "file2.txt")
