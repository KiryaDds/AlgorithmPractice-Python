#

class CustomSet:
    """Клас, що є множиною чисел та рядків.

    """

    def __init__(self, S):
        """Конструктор CustomSet з елементами str|int|float.

        """
        if isinstance(S, CustomSet):
            self.lstSet = S.lstSet[:]
        elif isinstance(S, str) or \
                isinstance(S, int) or \
                isinstance(S, float):
            self.lstSet = [S]
        elif isinstance(S, list):
            self.lstSet = []
            for e in S:
                if isinstance(e, str) or \
                        isinstance(e, int) or \
                        isinstance(e, float):
                    if e not in self.lstSet:
                        self.lstSet.append(e)
                else:
                    print("CustomSet : Елемент вхідного списку недопустимого типу !")
                    raise TypeError
        else:
            print("CustomSet : Вхідний параматр НЕ CustomSet|str|int|float|list !")
            raise ValueError

    def __len__(self):
        """Кількість елементів множини.

        """
        n = 0
        while True:
            try:
                e = self.lstSet[n]
                n += 1
            except IndexError:
                break
        return n

    def __add__(self, other):
        """Об’єднання множин.

        """
        if isinstance(other, CustomSet) or \
                isinstance(other, str) or \
                isinstance(other, int) or \
                isinstance(other, float):
            other_ = CustomSet(other)
        else:
            print("CustomSet.__add__ :Правий операнд недопустипого типу !")
            raise TypeError

        if len(self.lstSet) == 0:
            return other_
        elif len(other_.lstSet) == 0:
            return self
        else:
            for PL in self.lstSet:
                if PL not in other_.lstSet:
                    other_.lstSet.append(PL)
            return other_

    def __sub__(self, other):
        """Різниця множин.

        """
        if isinstance(other, CustomSet) or \
                isinstance(other, str) or \
                isinstance(other, int) or \
                isinstance(other, float):
            other_ = CustomSet(other)
        else:
            print("CustomSet.__sub__ :Правий операнд недопустипого типу !")
            raise TypeError

        if len(self.lstSet) == 0:
            other_.lstSet.clear()
            return other_
        elif len(other_.lstSet) == 0:
            other_.lstSet = self.lstSet[:]
            return other_
        else:
            A = self.lstSet[:]
            for PR in other_.lstSet:
                for i, PL in enumerate(A):
                    if PL == PR: del A[i:i + 1]
            return CustomSet(A)

    def __mul__(self, other):
        """Перетин множин.

        """
        if isinstance(other, CustomSet) or \
                isinstance(other, str) or \
                isinstance(other, int) or \
                isinstance(other, float):
            other_ = CustomSet(other)
        else:
            print("CustomSet.__mul__ :Правий операнд недопустипого типу !")
            raise TypeError

        if len(self.lstSet) == 0 or len(other_.lstSet) == 0:
            other_.lstSet.clear()
            return other_
        else:
            A = []
            for PL in self.lstSet:
                if PL in other_.lstSet:
                    A.append(PL)
            return CustomSet(A)

    def __truediv__(self, other):
        """Симетрична різниця множин.

        """
        if isinstance(other, CustomSet) or \
                isinstance(other, str) or \
                isinstance(other, int) or \
                isinstance(other, float):
            other_ = CustomSet(other)
        else:
            print("CustomSet.__truediv__ :Правий операнд недопустипого типу !")
            raise TypeError

        if len(self.lstSet) == 0:
            return other_
        elif len(other_.lstSet) == 0:
            return self
        else:
            A = self - other_
            B = other_ - self
            A = A + B
            return A

    def __str__(self):
        """Друк об'єкта.

        """
        n = len(self.lstSet)
        if n == 0:
            return "Пуста множина"
        else:
            S = ""
            i = False
            for e in self.lstSet:
                if i:
                    S += " U "
                else:
                    i = True
                if isinstance(e, int) or isinstance(e, float): e = str(e)
                S += e
            return S


if __name__ == "__main__":
    #  Тестування множини :
    M1 = CustomSet([1, 3, 4, 102])
    print("M1:", M1)
    M2 = CustomSet([3, 4, 1.23, "ass"])
    M3 = CustomSet([102, -10.5, 102.8, 1, "fff", "abnb", -8])
    MP = M1 + M2
    print("MP:", MP)
    MM = M2 - M1
    print("MM:", MM)
    MQ = M2 * M1
    print("MQ:", MQ)
    MR = M2 / M3
    print("MR:", MR)
