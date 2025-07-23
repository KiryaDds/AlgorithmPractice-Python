# Завдання 13.19 by  Янголь Ярослав / Комп. мех / 2 курс


class Polynom:
    """ Клас для моделювання роботи з поліномами"""

    def __init__(self, poly=None):
        """ Конструктор """
        self._coeffs = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        if poly is None:
            pass
        elif isinstance(poly, Polynom):      # Копіювання
            for i in poly._coeffs.keys():
                self._coeffs[i] = poly._coeffs[i]
        elif isinstance(poly, int) or isinstance(poly, float):
            self._coeffs[0] = poly
        elif isinstance(poly, dict):
            for i in poly.keys():
                self._coeffs[i] = poly[i]   # словник коефіцієнтів

    def clear(self):
        self._coeffs = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

    def __setitem__(self, power, coef):
        """ Встановлює коефіцієнт при відповідному степені
        :param power: степінь
        :param coef: коефіцієнт
        """
        self._coeffs[power] = coef

    def __getitem__(self, item):
        """ Квадратні дужки для читання/запису
        :param item: степінь
        :return: коефіцієнт
        """
        return self._coeffs[item] if item in self._coeffs.keys() else 0

    def __str__(self, var_sign="x"):
        """
        
        """
        s = ''
        for x in range(0, len(self._coeffs)+1):
            if x == 0:
                if self[x] > 0:
                    s = '+' + str(self[0]) + s
                elif self[x] < 0:
                    s = '-' + str(self[0]) + s
            elif x == 1:
                if self[x] > 0:
                    s = '+' + str(self[x]) + '*' + var_sign + s
                elif self[x] < 0:
                    s = '-' + str(-self[x]) + '*' + var_sign + s
            elif self[x] > 0:
                s = '+' + str(self[x]) + '*' + var_sign + '^' + str(x) + s
            elif self[x] < 0:
                s = '-' + str(-self[x]) + '*' + var_sign + '^' + str(x) + s

        if s == '':
            return "0"
        else:
            return s.lstrip('-').lstrip('+')

    def __add__(self, other):
        res = Polynom()
        if isinstance(other, Polynom):
            for x in self._coeffs.keys():
                if x in other._coeffs.keys():
                    res[x] = self[x] + other[x]
            return res

        elif isinstance(other, int) or isinstance(other, float):
            res = Polynom()
            if 0 in self._coeffs.keys():
                res[0] += other
            else:
                res[0] = other
            return res

    def __mul__(self, other):
        res = Polynom()
        if isinstance(other, Polynom):
            for x in self._coeffs.keys():
                for y in other._coeffs.keys():
                    if x+y in res._coeffs.keys():
                        res[x + y] += self[x] * other[y]
                    else:
                        res[x + y] = self[x] * other[y]
            return res

        elif isinstance(other, int) or isinstance(other, float):
            res = Polynom(self)
            for x in self._coeffs.keys():
                res[x] *= other
            return res

    @property
    def el(self):
        return self._coeffs
    

class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            exit(1)
        else:
            return self.items.pop()
    
    def back(self):
        if len(self.items) == 0:
            exit(1)
        else:
            return self.items[-1]
    
    def size(self):
        return self.items.count("n")
    
    def clear(self):
        self.items.clear()


def static_complexity():

    def mister_looper():

        while True:

            global binom, x
            line = list(map(str, input().split()))

            if line[0] == "OP":
                if not "n" in line[1]:
                    x = Polynom({0: int(line[1])})
                else:
                    x = Polynom({1: 1})

            elif line[0] == "LOOP":
                if str(x) != "0":
                    st.push(x)
                    x = Polynom()
                st.push(line[1])

            elif line[0] == "END":
                multipl = st.pop()
                if multipl == "BEGIN":
                    binom = binom + x
                    break
                if "n" in multipl:
                    multipl = Polynom({1: 1})
                    if str(binom) != "0":
                        binom = (binom + x) * multipl
                    else:
                        binom = x * multipl
                else:
                    if str(binom) != "0":
                        binom = (binom + x) * int(multipl)
                    else:
                        binom = x * multipl
                if isinstance(st.back(), Polynom):
                    binom = binom + st.pop()
            
        return


    global binom, x
    binom = Polynom()
    x = Polynom()
    st = Stack()
    
    k = int(input())
    for j in range(1, k + 1):

        print("Program #", str(j), sep="")
        st.push(input())
        
        mister_looper()

        print("Runtime =", binom.__str__("n"))
        if j != k:
            print()
        binom.clear()
        st.clear()
        x.clear()


if __name__ == "__main__":

    static_complexity()