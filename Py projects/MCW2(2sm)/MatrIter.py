# У цьому файлі реалізується iterator для матриці


class MatrIter:
    """Ітератор для проходження елементів послідовності матриці за правилом.

    """

    def __init__(self, data):

        Lr = []
        for e in data:
            if isinstance(e, list):
                Lr.append(e)
            else:
                print("IterIFS : Елемент вхідної послідовності недопустимого типу !")
                raise TypeError

        def MatrSort(ls):
            n = len(ls)
            n_ls = []
            for i in range(n):
                n_r = []
                for j in range(n):
                    if j == i and i != n-1:
                        n_r.append(ls[i+1][j-i])
                    else:
                        n_r.append(ls[i][n-j-1])
                n_ls.append(n_r)
            return n_ls

        self._data = MatrSort(Lr)  # _data - дані (послідовність)
        self._index = 0  # index - індекс поточного елемента послідовності   m = list(...);  list[i]
        self._n = len(self._data)  # n - кількість елементів

    def __iter__(self):
        return self

    def __next__(self):
        try:
            e = self._data[self._index]
            self._index += 1
            return e
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    '''
2 3 -7
4 5 6
-10 -1 -3 Matrix for task.txt
    '''
    u = [[1, 2, 3], [0, 9, 4]]
    a = MatrIter(u)
    for i in a:
        print(i)