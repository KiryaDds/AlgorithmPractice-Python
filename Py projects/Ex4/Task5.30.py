n = int(input("n = "))
for i in range(1, n + 1):
    p = 1
    for j in range(1, i + 1):
        p *= j
    if i >= 3:
        a = int(p ** (1 / 3))
        while (a - 1) * a * (a + 1) < p:
            a += 1
        if (a - 1) * a * (a + 1) == p:
            print("\033[32m{}! \033[0m= \033[34m{} \033[0m= \033[35m{} \033[0m* \033[35m{} \033[0m* \033[35m{}"
                  .format(i, p, a - 1, a, a + 1))

non_stop = input()
