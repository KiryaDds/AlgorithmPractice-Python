# Модуль, що реалізує клас мультимножини.
# Додано виключення.

class MSetParamError(Exception):
        """Помилка введення параметру в M_set(p)

        """

        def __init__(self, dd):
            self._dd = dd

        def __str__(self):
            return "Wrong parameter instance: M_set(%s)\nAllowed types: dict, M_set." % self._dd


class MSetValueError(Exception):
    """Помилка значення параметру n в класі M_set

    """
    def __init__(self, n):
        self._n = n

    def __str__(self):
        return "Wrong value: n = %s. Must be n > 0." % self._n


class MSetAddError(Exception):
    """Помилка значення параметру k в методі класу M_set

    """
    def __init__(self, k):
        self._k = k

    def __str__(self):
        return 'No such elements "%s" in M_set!' % self._k


class M_set:
    """Клас для реалізації мультимножини.

    """

    def __init__(self, dd={}):
        if isinstance(dd, M_set):
            self.d = {}
            try:
                for k, n in dd.d.items():
                    if n <= 0:
                        raise MSetValueError(n)
                    else:
                        self.d[k] = n

            except ValueError:
                # global n
                print("Wrong parameter instance: n = %s. Must be intenger n > 0." % n)

        elif isinstance(dd, dict):
            self.d = dd.copy()      # Опис словника {k:n}

            '''
            lst_for_del = []
            for k, n in self.dd.items():
                if not (isinstance(n, int)) or n <= 0: lst_for_del.append(k)
            for i in lst_for_del: del self.d[i]
            '''

        else:
            raise MSetParamError(dd)

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
        try:
            if n < 0:
                raise MSetValueError(n)
            else:
                if self.d.get(k) is None:
                    self.d.update({k: n})
                else:
                    self.d[k] += n

                if self.d[k] <= 0:
                    del self.d[k]

        except ValueError:
            print("Wrong parameter instance: n = %s. Must be intenger n > 0." % n)

    def remove(self, k):
        """Забирає та повертає один елемент "k" з мультимножини.

        """
        try:
            if self.d.get(k) is None:
                raise MSetAddError(k)
            elif self.d[k] == 1:
                del self.d[k]; return k, 1
            else:
                 self.d[k] -= 1; return k, 1

        except ValueError:
            print("Wrong parameter instance: n = %s. Must be intenger n > 0." % self.d[k])

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
        try:
            for k, n in self.d.items():
                if (isinstance(n, int) and n > 0) or self.is_empty():
                    i += 1
                    s += '"' + (k if isinstance(k, str) else str(k)) + '":' + str(n) + "; "
                    if i == 10:
                        s += "\n"; i = 0
                else:
                    del self.d[k]
                    raise MSetValueError(n)

        except ValueError:
            # global n
            print("Wrong parameter instance: n = %s. Must be intenger n > 0." % n)
        finally:
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

    #ParamErrorTest1 = M_set(132)
    #ParamErrorTest2 = M_set([0, "9", 4])
    ParamErrorTest3 = M_set({"key": -1})
    #print(ParamErrorTest1)
    #print(ParamErrorTest2)
    print(ParamErrorTest3)
