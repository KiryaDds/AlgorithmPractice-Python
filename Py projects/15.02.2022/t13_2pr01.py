# t13_2pr01.py
"""Тема 13. СЛАСИ І ОБ'ЄКТИ
  Задача 9.5 За допомогою класів Точка,Відрізок розв’язати наступні задачі.
    У текстовому файлі записано послідовність точок. Знайти:
     a) трикутник з найбільшою площею, утворений точками послідовності;
     b) коло найменшого радіуса, всередині якого лежать всі точки послідовності;
     c) відрізок, на якому лежить найбільша кількість точок послідовності.
"""
EPS = 1e-12


# При Sтрик(t1,t2,t3) < EPS вважаємо, що Sтрик(t1,t2,t3)=0
#   і t1,t2,t3 належать прямій

def _EP(p):
    return '\n' if p else ''


def _det3(A):
    """Детермінант матриці A розмірністью 3*3.

       A представлена у вигляді одновимірного вектора (по рядкам).
    """
    d = 0
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0]*A[1][1] - A[1][0]*A[0][1]

    for fc in indices:
        As = A.copy()
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1)**(fc % 2)
        sub_det = _det3(As)
        d += sign * A[0][fc] * sub_det

    return d


class Point:
    """Клас точка.

    """

    def __init__(self):
        """Конструктор точки.

        """
        self.x = None
        self.y = None
        self.name = None

    def get_point(self):
        """Взяти точку.

        """
        return float(self.x), float(self.y)

    def put_point(self, put=False, name=None):
        """Показати  точку.

           При put - друкуємо ім'я точки name і координати (x,y),
               інакше друкуємо тільки (x,y)
        """
        if put: print(name, end='')
        print('(', end=''); print(self.x, end='')
        print(',', end=''); print(self.y, end='')
        print(')')

    def set_point(self, x, y, name=None):
        """Покласти точку рівною (x, y).

        """
        self.x = x
        self.y = y
        self.name = name


class Segment:
    """Клас відрізок.

    """
    def __init__(self, a=None, b=None):
        """Конструктор класу.

        """
        self._a = a
        self._b = b
        self._name = None

    def get_segment(self):
        """Взяти відрізок.

        """
        return self._a, self._b

    def put_segment(self, put=False, name=None):
        """Показати відрізок.

        """
        x1, y1 = self._a.get_point()
        x2, y2 = self._b.get_point()
        if put: print(name, end='')
        print('[(%6f, %6f);(%6f, %6f)]' % (x1, y1, x2, y2))

    def set_segment(self, a, b, name=None):
        """Покласти відрізок рівним a, b.

        """
        self._a = a
        self._b = b
        self._name = name

    def len_segment(self):
        """Довжина відрізку.

        """
        xa, ya = self._a.get_point()
        xb, yb = self._b.get_point()
        d = ((xb - xa)**2 + (yb - ya)**2)**(1/2)
        return d

    def square_triangle(self, t):
        """Площа трикутника, утвореного точкою t та відрізком s.

        """
        if self.in_line(t):
            return 0
        else:
            xa, ya = self._a.get_point()
            xb, yb = self._b.get_point()
            xt, yt = t.get_point()
            S = ((xt - xa)*(yb - ya) - (yt - ya)*(xb - xa))/2
            if S < 0:
                S = -S
            if S < EPS:
                S = 0
            return S

    def in_line(self, t):
        """? чи лежить точка t на одній прямій з відрізком s.

        """
        xa, ya = self._a.get_point()
        xb, yb = self._b.get_point()
        xt, yt = t.get_point()
        S = ((xt - xa)*(yb - ya) - (yt - ya)*(xb - xa))/2
        return S == 0

    def in_segment(self, t):
        """? чи лежить точка t всередині відрізку s.

        """
        if self.in_line(t):
            ab = Segment()
            at = Segment()
            tb = Segment()
            ab.set_segment(self._a, self._b)
            at.set_segment(self._a, t)
            tb.set_segment(t, self._b)
            return ab.len_segment() != abs(at.len_segment() - tb.len_segment()) and\
                (at.len_segment() != 0 and tb.len_segment() != 0)


def _par_Circle(t1, t2, t3):
    """Визначення параметрів Z,R кола, побудованого по точкам t1,t2,t3.
    """
    # знаходимо загальне рівняння кола: x**2+y**2+A*x+B*y+C=0,
    #   тоді Z = (-0.5*A,-0.5*B), R = srqt(A*A+B*B-4*C),
    #   а отже  (x-Z.x)**2+(y-Z.y)**2=R**2

    Z = Point()
    AB = Segment(t1, t2); BC = Segment(t2, t3); AC = Segment(t3, t1)
    if AB.in_line(t3): return None, -1
    a = AB.len_segment(); b = BC.len_segment(); c = AC.len_segment()
    P = a + b + c
    x1, y1 = t1.get_point(); x2, y2 = t2.get_point(); x3, y3 = t3.get_point()
    Z.set_point((a*x1+b*x2+c*x3)/P, (a*y1+b*y2+c*y3)/P)
    AZ = Segment(Z, t1); R = AZ.len_segment()

    return Z, R


def pr_a(Lst_p):
    """трикутник з найбільшою площею, утворений точками послідовності Lst_p.

    """

    ij_seg = Segment()
    MaxSum = -1; i = 0; j = 0 ; k = 0
    n = len(Lst_p)
    if n == 0: return i, j, k, MaxSum
    else:
        for it, ip in enumerate(Lst_p):
            for jp in Lst_p[it + 1:]:
                for kp in Lst_p[it + 2:]:
                    ij_seg.set_segment(ip, jp)
                    if not ij_seg.in_line(kp):
                        Sum = ij_seg.square_triangle(kp)
                        if Sum > MaxSum:
                            MaxSum = Sum
                            i = it
                            j = Lst_p.index(jp)
                            k = Lst_p.index(kp)

        return i, j, k, MaxSum


def pr_b(Lst_p):
    """коло найменшого радіуса, всередині якого лежать всі точки послідовності Lst_p.

    """
    n = len(Lst_p)
    if n == 0: return None, -1

    nice_circles = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                f = True

                t0, R = _par_Circle(Lst_p[i], Lst_p[j], Lst_p[k])
                if t0 is None or R == -1: continue

                for p in Lst_p:
                    dist = Segment(p, t0)
                    if dist.len_segment()**2 > R**2:
                        f = False
                if f: nice_circles.append((t0, R))
    #print(nice_circles)

    t0 = None; R = None; first = True
    for r in nice_circles:
        if first: t0, R = r[0], r[1]; first = False
        if R > r[1]:
            t0, R = r[0], r[1]

    return t0, R


def pr_c(Lst_p):
    """відрізок, на якому лежить найбільша кількість точок послідовності Lst_p.

    """
    Klist = []
    n = len(Lst_p)
    if n == 0: return None, -1

    for i in range(n):
        for j in range(n):
            Seg = Segment(Lst_p[i], Lst_p[j])
            MaxK = 0
            for k in Lst_p:
                if Seg.in_segment(k): MaxK += 1
            Klist.append((Seg, MaxK))

    MaxK = -1; Seg = None
    for K in Klist:
        if K[1] > MaxK:
            Seg, MaxK = K[0], K[1]

    return Seg, MaxK


def txtf_to_Lp(namef):
    """Читання з текстового файлу namef послідовності точок Lst_p.

    """
    import sys

    Lst_p = []
    try:
        newin = open(namef)
        oldin = sys.stdin
        sys.stdin = newin  # переназначаємо введення
        newout = open("p" + namef, "w")
        oldout = sys.stdout
        sys.stdout = newout  # переназначаємо виведення

        i = 0
        while True:
            try:
                i += 1
                s = newin.readline().split()
                x = format(float(s[0]), '.6f')
                y = format(float(s[1]), '.6f')
                t = Point()
                t.set_point(x, y, "\nt%i" % i)
                Lst_p.append(t)
            except EOFError:
                break
            except ValueError:
                print("\nНеможливо конвертувати дані №%i в дійсне число." % i)
                continue

        sys.stdin = oldin  # відновлення станд.введення
        newin.close()

        sys.stdout = oldout  # відновлення станд.виведення
        newout.close()

    except FileNotFoundError as nf:
        print("Файл не знайдено:", nf.filename)
    except OSError as e:
        print("Помилка ОС")
        raise e
    except IOError as err:
        print("Помилка вводу/виводу (%s): %s" % (err.errno, err.strerror))
    except:
        print("Несподівана помилка:", sys.exc_info()[0])

    return Lst_p


if __name__ == "__main__":
    f = "t13_2pr01.txt"
    Lp = txtf_to_Lp(f)
    i = 0
    print("Послідовність точок площини :")

    for t in Lp:
        i += 1
        t.put_point(True, "t%i" % i)

    print("\n ЗАДАЧА a)")
    i, j, k, S = pr_a(Lp)
    if S == -1:
        print("Послідовність пуста !")
    elif S == 0:
        print("Всі точки послідовності лежать на одній прямій !")
    else:
        print("Трикутник, утворений точками :")
        Lp[i].put_point(True, "t%i" % (i + 1))
        Lp[j].put_point(True, "t%i" % (j + 1))
        Lp[k].put_point(True, "t%i" % (k + 1))
        print("має Max площу = %g" % S)

    print("\n ЗАДАЧА b)")
    t0, R = pr_b(Lp)
    if R == -1:
        print("Послідовність пуста !")
    elif R == 0:
        print("Всі точки послідовності однакові, тому :")
        t0.put_point(True, "центр кола")
        print("радіус = ", R)
    else:
        t0.put_point(True, "Коло з центром ")
        print("і Min радіусом = %g" % R,
              "містить всі точки послідовності")

    print("\n ЗАДАЧА c)")
    S, K = pr_c(Lp)
    if K == -1:
        print("Послідовність пуста !")
    elif K == 0:
        print("Жодний сегмент не містить інших точок послідовності.")
    else:
        S.put_segment(True, "Сегмент")
        print("містить Max кількість точок послідовності =%i" % K)
