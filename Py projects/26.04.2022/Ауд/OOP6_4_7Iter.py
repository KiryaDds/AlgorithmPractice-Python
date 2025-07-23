class IterIFS:
    """Ітератор для проходження елементів послідовності.

    """

    def __init__(self, data):
        """Конструктор необхідної послідовності.

        """
        Lint = []; Lfloat = []; Lstr = []
        for e in data :
            if   isinstance(e, int)   : Lint.append(e)
            elif isinstance(e, float) : Lfloat.append(e)
            elif isinstance(e, str)   : Lstr.append(e)
            else :
                print("IterIFS : Елемент вхідної послідовності недопустимого типу !")
                raise TypeError
        Lint.sort(); Lfloat.sort(); Lstr.sort()
        self._data = Lint + Lfloat[::-1] + Lstr  #_data - дані (послідовність)
        self._index = 0                          #_index - індекс поточного елемента послідовності
        self._n = len(self._data)                #_n - кількість елементів

    def __iter__(self):
        """Метод __iter__ повертає сам об'єкт як ітератор.

        """
        return self

    def __next__(self):
        """Метод __next__ повертає наступний елемент послідовності у порядку слідування.

        """
        if self._index == self._n:     #якщо дійшли до кінця послідовності
            raise StopIteration        #  ініціюєм виключення
        e = self._data[self._index]
        self._index += 1
        return e
        #  або така послідовність операторів
        '''
        try:
            e = self._data[self._index]
            self._index += 1
            return e
        except IndexError:
            raise StopIteration 
        '''


if __name__ == "__main__" :
    LL = [1, "ass", 102, 3, 4, 1.23, -10.5, 102.8, "fff", "abnb", -8]
    print("LL:\n", LL)
    L = IterIFS(LL)
    print("L:")
    for c in L:
        print(c, "", end='')
