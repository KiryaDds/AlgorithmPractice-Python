"""Т18.10 Описати клас-домішок CompareMixin, який реалізує усі 6 стандартних
   відношень (==, !=, <, >, <=, >=) на базі одного реалізованого відношення <
   та бульових операцій. Для цього треба реалізувати спеціальні методи __eq__,
   __ne__ тощо.
     Описати клас Point2 (точка площини) з властивостями – координатами та
   методами створення точки та виведення точки.
     Описати клас-нащадок Point2, який вводять порядок на точках (відношення <)
   та клас нащадок цього класу та домішку CompareMixin:
     а) XOrderPoint2 – впорядкування за першою координатою та
        FullXOrderPoint2 – всі відношення;
     б) YOrderPoint2 – впорядкування за другою координатою та
        FullYOrderPoint2 – всі відношення;
     в) DistOrderPoint2 –впорядкування за за відстанню від початку координат та
        FullDistOrderPoint2 – всі відношення.
     З використанням цих класів ввести список точок та показати їх у порядку
   незростання.
"""


class CompareMixin:
    def __eq__(self, value):
        return not self < value and not value < self
    def __ne__(self, value):
        return self < value or value < self
    def __gt__(self, value):
        return value < self
    def __le__(self, value):
        return not value < self
    def __ge__(self, value):
        return not self < value


class Point2:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class XOrderPoint2(Point2):
    def __lt__(self, value):
        return self._x < value.x


class YOrderPoint2(Point2):
    def __lt__(self, value):
        return self._y < value.y


class DistOrderPoint2(Point2):
    def __lt__(self, value):
        return (self.x**2+self.y**2)**(1/2) < (value.x**2+value.y**2)**(1/2)


class FullXOrderPoint2(CompareMixin, XOrderPoint2):
    pass


class FullYOrderPoint2(CompareMixin, YOrderPoint2):
    pass


class FullDistOrderPoint2(CompareMixin, DistOrderPoint2):
    pass


if __name__ == "__main__" :
    n = int(input('n='))
    Ax = []
    Ay = []
    Ad = []
    for i in range(n):
        x = float(input('x='))
        y = float(input('y='))
        px = FullXOrderPoint2(x, y)
        py = FullYOrderPoint2(x, y)
        pd = FullDistOrderPoint2(x, y)
        Ax.append(px)
        Ay.append(py)
        Ad.append(pd)

    Bx = []
    By = []
    Bd = []
    while Ax != []:
        mx = max(Ax)
        my = max(Ay)
        md = max(Ad)
        Bx.append(mx)
        By.append(my)
        Bd.append(md)
        Ax.remove(mx)
        Ay.remove(my)
        Ad.remove(md)

    print('FullXOrderPoint2 result (від най-> x до най-<):')
    for i in Bx:
        print('({},{})'.format(i.x, i.y))
    print('FullYOrderPoint2 result (від най-> y до най-<):')
    for i in By:
        print('({},{})'.format(i.x, i.y))
    print('FullDistOrderPoint2 result (від най-> за відстанню до початку координат до най-<):')
    for i in Bd:
        print('({},{})'.format(i.x, i.y))
