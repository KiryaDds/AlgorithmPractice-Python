# У цьому файлі реалізується завдання 6.3.2.

from Rational import *


class RatIter:
    """Ітератор для проходження елементів послідовності.

    """

    def __init__(self, data):
        """Конструктор необхідної послідовності.

        """
        Lr = []
        for e in data:
            if isinstance(e, Rational):
                Lr.append(e)
            else:
                print("IterIFS : Елемент вхідної послідовності недопустимого типу !")
                raise TypeError

        def RatSort(ls):
            for i in range(len(ls)):
                for j in range(0, len(ls) - i - 1):
                    if ls[j]["d"] < ls[j + 1]["d"]:
                        ls[j], ls[j + 1] = ls[j + 1], ls[j]
                    elif ls[j]["d"] == ls[j + 1]["d"]:
                        if ls[j]["n"] < ls[j + 1]["n"]:
                            ls[j], ls[j + 1] = ls[j + 1], ls[j]
            return ls

        self._data = RatSort(Lr)                # _data - дані (послідовність)
        self._index = 0                         # index - індекс поточного елемента послідовності
        self._n = len(self._data)               # n - кількість елементів

    def __iter__(self):
        """Метод __iter__ повертає сам об'єкт як ітератор.

        """
        return self

    def __next__(self):
        """Метод __next__ повертає наступний елемент послідовності у порядку слідування.

        """

        try:
            e = self._data[self._index]
            self._index += 1
            return e
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    Ln = ["-25/5", -9, "-2/16", -1, "-12/7", "13/14", "17/7", 24, "3/14", "5/22", "9/14", "3/8"]
    Lr = []
    for i in Ln:
        r = Rational(i)
        Lr.append(r)
    print("\nСписок скорочених дробів Lr:")
    for c in Lr:
        print(c, "", end='')
    L = RatIter(Lr)
    print("\n\nВідсортований список L:")
    for c in L:
        print(c, "", end='')
    print("\n")
