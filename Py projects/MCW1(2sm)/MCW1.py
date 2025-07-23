# Файл до виконання завданнь з модульної контрольної роботи
# Янголь Ярослав/Комп мех/1 курс

# class MatrixError(Exception):

class Matrix():
    """Реалізує матрицю

    """
    def __init__(self, matr=[]):
        if len(matr) == 0: self._lst = None
        elif not isinstance(matr, list): raise Exception
        else:
            self._lst = matr.copy()
            self._m, self._n = len(matr[0]), len(matr)

    @staticmethod
    def create_matrix(self, m, n):
        """"""
        rows = []
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(0)
            rows.append(nums)
        self._lst = rows
        self._m = m
        self._n = n

    def size(self):
        """"""
        return self._m, self._n

    def __getitem__(self, item):
        """"""
        print(self._lst[item[0]][item[1]])
        return self._lst[item[0]][item[1]]

    @staticmethod
    def change_el(self, i, j, el):
        """"""
        self._lst[i][j] = el

    def __add__(self, other):
        other = Matrix(other)
        res = []
        nums = []
        for i in range(len(self._lst)):
            for j in range(len(self._lst[0])):
                nums.append(self._lst[i][j] + other._lst[i][j])
                if len(nums) == len(self._lst):
                    res.append(nums)
                    nums = []
        return Matrix(res)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self._lst]
            return Matrix(result)
        elif self._n != other._m:
            return 'Не можна перемножити матриці таких розмірів!'
        else:
            res = []
            for i in self._lst:
                res1 = []
                for j in other._lst:
                    el = 0
                    for k in self._lst[i]:
                        el += self._lst[i][k] * other._lst[k][j]
                    res1.append(el)
                res.append(res1)
            return Matrix(res)

    def __str__(self):
        s = "["
        m, n = self.size()
        for i in range(m):
            for j in range(n):
                if j != n: s += str(self[i, j]) + ", "
                else: s += str(self[i, j]) + ";\n"
        s += "]"
        return s


if __name__ == "__main__":
    A = Matrix([[1, 5, 4], [1, 5, 4]])
    print("Matrix A:", A)
    print("Its size:", A.size())
