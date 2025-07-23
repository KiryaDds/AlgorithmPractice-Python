# Завдання 2

import shelve


def dct_to_binf(prods, bin_f):
    f = shelve.open(bin_f)
    for i in prods.keys():
        f[i] = prods[i]
    f.close()


def pr_prod(store_name, nBD, nS):
    print("""               \033[036mПродукція на складі магазину {} \033[039m""".format(store_name))
    print("    \033[033mШтрих-код Найменування продукції" + "%+30s" % "Кількість\033[039m")
    with shelve.open(nBD) as nBD_l:
        with shelve.open(nS) as nS_l:
            for i in nBD_l.keys():
                diff = len("%+48s" % "Найменування продукції") - len(str(nS_l[i]))
                format_str = "%+{}s ".format(diff)

                print(str(i) + " \033[032m" + str(nS_l[i]) + format_str % "\033[034m" + str(nBD_l[i]) + "\033[039m")


def market(nBD, nM):
    nM_d = {}
    f = open(nM, "r")
    lines = f.readlines()
    for line in lines:
        line = line.split()
        if line[0] not in nM_d.keys():
            nM_d[line[0]] = int(line[1])
        else:
            nM_d[line[0]] = nM_d[line[0]] + int(line[1])
    f.close()
    with shelve.open(nBD) as nBD_l:
        for i in nBD_l.keys():
            nBD_l[i] = nBD_l[i] + nM_d[i]


if __name__ == "__main__" :
    nBD = "store_house"
    nS = "production"
    nM = "market.txt"
    D = {"4000000000111": 150, "4000000002111": 50, "4000000003111": 350}
    dct_to_binf(D, nBD)
    S = {"4000000000111": 'Папір А4',
         "4000000002111": 'OIL GEL PEN (Sigma)',
         "4000000003111": 'Календар "Для кишені"'}
    dct_to_binf(S, nS)
    print()
    pr_prod('"Є все"', nBD, nS)
    market(nBD, nM)
    print("\n\033[035mОновлення виконано!\033[039m\n")
    pr_prod('"Є все"', nBD, nS)
