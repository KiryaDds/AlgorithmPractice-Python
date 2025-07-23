class Segm:
    def __init__(self):
        self.a = None
        self.b = None
        self.empty = True

    def _setempty(self):
        """Означення поля empty.

        """
        return self.a > self.b

    def emptySegm(self):
        """Зробити відрізок порожнім.

        """
        self.empty = True

    def is_empty(self):
        """? чи порожній відрізок.

        """
        return self.empty

    def set_Segm(self, a, b):
        """Покласти відрізок рівним a, b.

        """
        self.a = a
        self.b = b
        self.empty = self._setempty()

    def crossingSegm(self, P):
        """Перетин об'єкту з відрізком Р.

        """
        S = Segm()
        if self.is_empty() or P.is_empty():
            pass
        else:
            l = max(self.a, P.a)
            r = min(self.b, P.b)
            S.set_Segm(l, r)
        return S

    def __str__(self):
        """Друк об'єкту.

        """
        if self.is_empty():
            return "Пустий відрізок"
        else:
            return '[%g,%g]' % (self.a, self.b)


if __name__ == "__main__":
    A = Segm(); print("A=", A)
    A.set_Segm(4, 3); print("A=", A)
    A.set_Segm(3, 5); print("A=", A)
    B = Segm();B.set_Segm(4, 15); print("B=", B)
    C = A.crossingSegm(B); print("C=", C)
    C.emptySegm(); print("C=", C)
