# Модуль, що реалізує клас мультимножини.

class M_set:
    """Клас для реалізації мультимножини.

    """

    def __init__(self, dd={}):
        if isinstance(dd, M_set):
            self.d = {}
            for k, n in dd.d.items():
                self.d[k] = n
        elif isinstance(dd, dict):
            self.d = dd.copy()      # Опис словника {k:n}
        elif isinstance(dd, str):
            self.d.update({dd: 1})
        elif isinstance(dd, int or float):
            self.d.update({str(dd): 1})
        elif isinstance(dd, list or tuple or set):
            for n, k in enumerate(dd):
                k = k if isinstance(k, str) else str(k)
                if k not in self.d.keys():
                    self.d.update({k: n})
                else:
                    self.d[k] += n

    def clear_set(self):
        """Робить мультимножину порожньою.

        """
        self.d.clear()

    def is_empty(self):
        """Визначає чи є мультимножина пустою.

        """
        return len(self.d) == 0

    def add(self, k, n=1):
        """Додає новий елемент "k" (у кількості n) до мультимножини.

        """
        if self.d.get(k) is None:
            self.d.update({k: n})
        else:
            self.d[k] += n
        if self.d[k] <= 0:
            del self.d[k]

    def remove(self, k):
        """Забирає та повертає один елемент "k" з мультимножини.

        """
        if self.d.get(k) is None:
            print("remove: Error: No such elements in M_set", k)
        elif self.d[k] == 1:
            del self.d[k]; return k, 1
        else:
             self.d[k] -= 1; return k, 1

    def count(self, k):
        """Визначає кількість входжень елементу k до мультимножини.

        """
        return 0 if self.d.get(k) is None else self.d[k]

    def ms_union(self, m):
        """Об’єднання двох мультимножин.

        """
        if self.is_empty(): res = M_set(m)
        elif m.is_empty(): res = M_set(self.d)
        else:
            res = M_set(m)
            for k, n in self.d.items():
                e = res.count(k)
                res.add(k, -e + max(e, n))

        return res

    def ms_intersect(self, m):
        """Перетин двох мультимножин.

        """
        res = M_set()
        if not(self.is_empty() or m.is_empty()):
            for k, n in self.d.items():
                e = m.count(k)
                if e > 0:
                    res.add(k, min(e, n))

        return res

    def __str__(self):
        """Друк мультимножини.

        """
        s = ""; i = 0
        for k, n in self.d.items():
            i += 1
            s += '"' + (k if isinstance(k, str) else str(k))\
                 + '":' + str(n) + "; "
            if i == 10:
                s += "\n"; i = 0
        return s


if __name__ == "__main__":
    A = "fdp55555ddffff9090"
    Aset = M_set()
    print("Пуста мультимножина Aset\n", Aset)
    for s in A:
        Aset.add(s)
    print("Мультимножина Aset\n", Aset)

    B = ("5", "3", "3", "0", "8", "f", "f", "f", "f", "f", "d")
    Bset = M_set()
    for s in B:
        Bset.add(s)
    print("Мультимножина Bset\n", Bset)

    Cset = Aset.ms_union(Bset)
    print("Мультимножина Cset = Aset|Bset\n", Cset)

    Cset.clear_set()
    print("Мультимножина Cset = \n", Cset)
    if Cset.is_empty():
        print("Є пуста мультимножина!")

    Cset = Aset.ms_intersect(Bset)
    print("Мультимножина Cset = Aset&Bset\n", Cset)

    Cset.count("f")
    for i in range(Cset.count("f")):
        Cset.remove("f")
    Cset.count("f")

    print("Мультимножина Cset після перетворень (видалено всі 'f') =  \n", Cset)
