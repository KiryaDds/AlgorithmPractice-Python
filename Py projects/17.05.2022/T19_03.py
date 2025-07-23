"""Т19.3 Описати абстрактний клас Shape (геометрична фігура) та його
   нащадки Circle (коло), Rectangle (прямокутник), Triangle (трикутник).
   Передбачити у Shape властивості обчислення периметру та площі фігури,
   а також метод, що перевіряє, чи перетинаються дві фігури.
       З використанням цих класів розв’язати задачу:
          Дано список геометричних фігур, що не перетинаються.
          Перевірити, чи справді вони не перетинаються та
          порахувати загальний периметр і сумарну площу.
"""

from abc import ABCMeta, abstractmethod
from math import pi, sqrt


class Shape(metaclass=ABCMeta):
    @property
    @abstractmethod
    def Per(self):
        """Периметр фігури.
        """
        pass

    @property
    @abstractmethod
    def Area(self):
        """Площа фігури.
        """
        pass

    @abstractmethod
    def CrossShape(self, other):
        """? Перетинаються фігури self, other.
        """
        pass


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self, name=""):
        return name + "(%g,%g)" % (self.x, self.y)

    @staticmethod
    def dist(A, B):
        """Віддаль між точками A,B.
        """
        x = A.x - B.x
        y = A.y - B.y
        return sqrt(x * x + y * y)

    @staticmethod
    def line(M1, M2):
        """Пряма L≡A*x+B*y+C=0, яка проходить через M1,M2.
        """
        A = M2.y - M1.y
        B = M1.x - M2.x
        C = -A * M1.x - B * M1.y
        return A, B, C

    @staticmethod
    def dist_line(T, M1, M2):
        """Відстань від точки T до прямої L≡A*x+B*y+C=0, яка проходить через M1,M2.
        """
        A, B, C = Point.line(M1, M2)  # Коефіцієнти прямої L
        return abs((A * T.x + B * T.y + C) / sqrt(A * A + B * B))

    @staticmethod
    def sq_3(T, A, B):
        """Площа ▲(T,A,B) "зі знаком".
        """
        a = A.x * B.y - A.y * B.x
        b = T.y * B.x - T.x * B.y
        c = T.x * A.y - T.y * A.x
        return 0.5 * (a + b + c)

    @staticmethod
    def T_in_Conv(T, LP):
        """? Чи є точка T внутріньою для опуклої оболонки LP.
        """
        n = len(LP)
        Yes = True
        for i in range(n + 1):
            j = 0 if i == n else i + 1
            Yes = Yes and Point.sq_3(T, LP[i], LP[j]) <= 0
        return Yes

    @staticmethod
    def crs_line(L1, L2):
        """? Чи перетинаються прямі L1 і L2, задані рівнянням L≡A*x+B*y+C=0.
        """
        d = L1[0] * L2[1] - L1[1] * L2[0]  # Визначник СЛАР
        if d == 0:
            if L1[0] * L2[2] == L2[0] * L1[2] and L1[1] * L2[2] == L2[1] * L1[2]:
                return True  # СЛАР сумісна, безліч розв'язків
            else:
                return False  # СЛАР несумісна, розв'язків немає
        else:
            return True  # СЛАР сумісна, один розв'язок


class Circle(Shape):
    def __init__(self, C, R):
        self.Z = Point(C.x, C.y)
        self.R = R

    @property
    def Xcentre(self):
        return self.Z.x

    @property
    def Ycentre(self):
        return self.Z.y

    @property
    def Radius(self):
        return self.R

    def __str__(self, name=""):
        C = self.Z
        return "○" + name + "{" + C.__str__("C") + ";%f}" % self.R

    @property
    def Per(self):
        return 2 * pi * self.R

    @property
    def Area(self):
        return pi * self.R * self.R

    @staticmethod
    def in_C(C, T):
        """? Точка T в середині кола C.
        """
        return Point.dist(T, C.Z) <= C.R

    @staticmethod
    def C_in(C, M1, M2):
        """? Центр кола C під відрізком [M1,M2].
        """
        if Point.dist_line(C.Z, M1, M2) <= C.R:
            lx = min(M1.x, M2.x)
            rx = max(M1.x, M2.x)
            ly = min(M1.y, M2.y)
            ry = max(M1.y, M2.y)
            if lx <= C.Xcentre <= rx and ly <= C.Ycentre <= ry: return True
        return False

    def CrossShape(self, other):
        if isinstance(other, Circle):
            return Point.dist(self.Z, other.Z) <= self.R + other.R
        elif isinstance(other, Rectangle):
            # Якась кутова точка ■ є ○
            if Circle.in_C(self, other.A):
                return True
            elif Circle.in_C(self, other.B):
                return True
            elif Circle.in_C(self, other.C):
                return True
            elif Circle.in_C(self, other.D):
                return True
            else:  # Центр ○ знаходиться всередині ■
                if Circle.C_in(self, other.A, other.B):
                    return True
                elif Circle.C_in(self, other.B, other.C):
                    return True
                elif Circle.C_in(self, other.C, other.D):
                    return True
                elif Circle.C_in(self, other.D, other.A):
                    return True
            return False
        elif isinstance(other, Triangle):
            # Якась кутова точка ▲ є ○
            if Circle.in_C(self, other.A):
                return True
            elif Circle.in_C(self, other.B):
                return True
            elif Circle.in_C(self, other.C):
                return True
            else:  # Центр ○ знаходиться всередині ▲
                if Circle.C_in(self, other.A, other.B):
                    return True
                elif Circle.C_in(self, other.B, other.C):
                    return True
                elif Circle.C_in(self, other.C, other.A):
                    return True
            return False
        else:
            raise TypeError("Правий операнд недопустипого типу!")


class Rectangle(Shape):
    def __init__(self, *T):
        self.A = T[0]
        self.B = T[1]
        self.C = T[2]
        self.D = T[3]
        self.a = None  # довжина сторони AB
        self.b = None  # довжина сторони AD
        self.len_side()

    def len_side(self):
        self.a = Point.dist(self.A, self.B)
        self.b = Point.dist(self.A, self.D)

    def __str__(self, name=""):
        a = self.A.__str__("A")
        b = self.B.__str__("B")
        c = self.C.__str__("C")
        d = self.D.__str__("D")
        return "■" + name + "{" + a + ";" + b + ";" + c + ";" + d + "}"

    @property
    def Per(self):
        return 2 * (self.a + self.b)

    @property
    def Area(self):
        return self.a * self.b

    def CrossShape(self, other):
        if isinstance(other, Circle):
            # Якась кутова точка ■ є ○
            if Circle.in_C(other, self.A):
                return True
            elif Circle.in_C(other, self.B):
                return True
            elif Circle.in_C(other, self.C):
                return True
            elif Circle.in_C(other, self.D):
                return True
            else:  # Центр ○ знаходиться всередині ■
                if Circle.C_in(other, self.A, self.B):
                    return True
                elif Circle.C_in(other, self.B, self.C):
                    return True
                elif Circle.C_in(other, self.C, self.D):
                    return True
                elif Circle.C_in(other, self.D, self.A):
                    return True
            return False
        elif isinstance(other, Rectangle):
            # Якась кутова точка ■2 є ■1
            LP = [self.A, self.B, self.C, self.D]
            if Point.T_in_Conv(other.A, LP) or \
                    Point.T_in_Conv(other.B, LP) or \
                    Point.T_in_Conv(other.C, LP) or \
                    Point.T_in_Conv(other.D, LP): return True
            # Якась кутова точка ■1 є ■2
            LP = [other.A, other.B, other.C, other.D]
            if Point.T_in_Conv(self.A, LP) or \
                    Point.T_in_Conv(self.B, LP) or \
                    Point.T_in_Conv(self.C, LP) or \
                    Point.T_in_Conv(self.D, LP): return True
            # Перетин ■1 i ■2 типу "хрест"
            if ...:

                return True
            return False
        elif isinstance(other, Triangle):
            # Якась кутова точка ▲ є ■
            LP = [self.A, self.B, self.C, self.D]
            if Point.T_in_Conv(other.A, LP) or \
                    Point.T_in_Conv(other.B, LP) or \
                    Point.T_in_Conv(other.C, LP): return True
            # Якась кутова точка ■ є ▲
            LP = [other.A, other.B, other.C]
            if Point.T_in_Conv(self.A, LP) or \
                    Point.T_in_Conv(self.B, LP) or \
                    Point.T_in_Conv(self.C, LP) or \
                    Point.T_in_Conv(self.D, LP): return True
            # Перетин ■ i ▲ типу "хрест"
            # if ... : return True
            return False
        else:
            raise TypeError("Правий операнд недопустипого типу!")


class Triangle(Shape):
    def __init__(self, *T):
        self.A = T[0]
        self.B = T[1]
        self.C = T[2]
        self.a = None  # довжина сторони BC
        self.b = None  # довжина сторони AC
        self.c = None  # довжина сторони AB
        self.len_side()

    def len_side(self):
        self.a = Point.dist(self.B, self.C)
        self.b = Point.dist(self.A, self.C)
        self.c = Point.dist(self.A, self.B)

    def __str__(self, name=""):
        a = self.A.__str__("A")
        b = self.B.__str__("B")
        c = self.C.__str__("C")
        return "▲" + name + "{" + a + ";" + b + ";" + c + "}"

    @property
    def Per(self):
        return self.a + self.b + self.c

    @property
    def Area(self):
        p = 0.5 * self.Per
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def CrossShape(self, other):
        if isinstance(other, Circle):
            # Якась кутова точка ▲ є ○
            if Circle.in_C(other, self.A):
                return True
            elif Circle.in_C(other, self.B):
                return True
            elif Circle.in_C(other, self.C):
                return True
            else:  # Центр ○ знаходиться всередині ▲
                if Circle.C_in(other, self.A, self.B):
                    return True
                elif Circle.C_in(other, self.B, self.C):
                    return True
                elif Circle.C_in(other, self.C, self.A):
                    return True
            return False
        elif isinstance(other, Rectangle):
            # Якась кутова точка ▲ є ■
            LP = [self.A, self.B, self.C]
            if Point.T_in_Conv(other.A, LP) or \
                    Point.T_in_Conv(other.B, LP) or \
                    Point.T_in_Conv(other.C, LP) or \
                    Point.T_in_Conv(other.D, LP): return True
            # Якась кутова точка ■ є ▲
            LP = [other.A, other.B, other.C, other.D]
            if Point.T_in_Conv(self.A, LP) or \
                    Point.T_in_Conv(self.B, LP) or \
                    Point.T_in_Conv(self.C, LP): return True
            # Перетин ▲ i ■ типу "хрест"
            # if ... : return True
            return False
        elif isinstance(other, Triangle):
            # Якась кутова точка ▲2 є ▲1
            LP = [self.A, self.B, self.C]
            if Point.T_in_Conv(other.A, LP) or \
                    Point.T_in_Conv(other.B, LP) or \
                    Point.T_in_Conv(other.C, LP): return True
            # Якась кутова точка ▲1 є ▲2
            LP = [other.A, other.B, other.C]
            if Point.T_in_Conv(self.A, LP) or \
                    Point.T_in_Conv(self.B, LP) or \
                    Point.T_in_Conv(self.C, LP): return True
            # Перетин ▲ i ▼ типу "зірка"
            # if ... : return True
            return False
        else:
            raise TypeError("Правий операнд недопустипого типу!")


# Задаємо список фігур
'''
Fig = [Circle(Point(1, 2), 2),
       Circle(Point(-1, -1), 1),
       Circle(Point(6, 0), 3),
       Triangle(Point(4, 4), Point(7, 4), Point(4, 8)),
       Rectangle(Point(-5, 0), Point(-2, 0), Point(-2, 2), Point(-5, 2)),
       Triangle(Point(-4, -4), Point(-7, -5), Point(-3, -5)),
       Rectangle(Point(0, -2), Point(3, -5), Point(4, -4), Point(1, -1))]
N = len(Fig)
'''


def shape_readf(fn):
    figl = []
    c = "Circle"
    tr = "Triangle"
    rec = "Rectangle"
    f = open(fn, "r")
    lines = f.readlines()
    for line in lines:
        line = line.split()
        lname = line.pop(0)
        line = [int(x) for x in line]
        if lname == c:
            figl.append(Circle(Point(line[0], line[1]), line[2]))
        elif lname == tr:
            figl.append(Triangle(Point(line[0], line[1]), Point(line[2], line[3]),
                                 Point(line[4], line[5])))
        elif lname == rec:
            figl.append(Rectangle(Point(line[0], line[1]), Point(line[2], line[3]),
                                  Point(line[4], line[5]), Point(line[6], line[7])))
        else:
            print("Unknown Shape!", line)
    f.close()
    return figl


def shape_writef(fn, figl):
    import sys

    stdout_fileno = sys.stdout
    sys.stdout = open(fn, 'w', encoding='UTF-8')

    N = len(figl)

    # Показати фігури
    print("Список фігур :")
    for i, F in enumerate(figl):
        print("ф_№%d" % i, F)
    print()

    # Перевірити, чи справді вони не перетинаються
    cross = False
    for i, f in enumerate(Fig[0:N]):
        j = i
        for F in Fig[i + 1:]:
            j += 1
            c = f.CrossShape(F)
            print("ф_№%d ∩ ф_№%d=" %(i, j), c)
            cross = cross or c
    print("Перетин для списку фігур =", cross)
    print()

    if not cross:  # якщо перетин = Ø, то знайдемо P, S
        PFig = 0; SFig = 0
        for i, F in enumerate(Fig):
            p = F.Per; s = F.Area
            print("ф_№%d: " % i, "p=", p, "s=", s)
            PFig += p; SFig += s
        print("Загальний периметр=", PFig,
              "\nЗагальна  площа   =", SFig)

    sys.stdout.close()
    sys.stdout = stdout_fileno
    print("Check \"%s\" file in directory." % fn)


f_in_name = "in.txt"
f_out_name = "out.txt"
Fig = shape_readf(f_in_name)
shape_writef(f_out_name, Fig)


'''
# Показати фігури
print("Список фігур :")
for i, F in enumerate(Fig):
    print("ф_№%d" % i, F)
print()

# Перевірити, чи справді вони не перетинаються
cross = False
for i, f in enumerate(Fig[0:N]):
    j = i
    for F in Fig[i + 1:]:
        j += 1
        c = f.CrossShape(F)
        # print("ф_№%d ∩ ф_№%d=" %(i, j), c)
        cross = cross or c
print("Перетин для списку фігур =", cross)
print()

if not cross:  # якщо перетин = Ø, то знайдемо P, S
    PFig = 0;
    SFig = 0
    for i, F in enumerate(Fig):
        p = F.Per;
        s = F.Area
        # print("ф_№%d: " % i, "p=", p, "s=", s)
        PFig += p;
        SFig += s
    print("Загальний периметр=", PFig,
          "\nЗагальна  площа   =", SFig)
'''
