def print_txtf(filename):
    f = open(filename)
    print("\nІм'я файлу = ", filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
    print()
    f.close()
