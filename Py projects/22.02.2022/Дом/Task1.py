# У файлі описано два класи: "Точка на екрані" та "Прямокутник на екрані".
# Також файл містить невеличке тестування роботи класів

import turtle


class Point:
    """Точка екрану

    """

    def __init__(self, x, y, clr="black", w=6):
        self._x = x  # _x - координата x точки
        self._y = y  # _y - координата y точки
        self._clr = clr  # _clr - колір точки
        self._w = w  # _w - товщина точки
        self._visible = False  # - видимість точки

    def getx(self):
        """Повертає координату x точки

        """
        return self._x

    def gety(self):
        """Повертає координату y точки

        """
        return self._y

    def getclr(self):
        """Повертає колір точки

        """
        return self._clr

    def getw(self):
        """Повертає товщину точки

        """
        return self._w

    def onscreen(self):
        """Перевіряє, чи є точка видимою на екрані

        """
        return self._visible

    def switchon(self):
        """Робить точку видимою на екрані

        """
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot(self._w, self._clr)
            turtle.up()

    def switchoff(self):
        """Робить точку невидимою на екрані

        """
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot(self._w, turtle.bgcolor())
            turtle.up()


class Priam:
    """Прямокутник екрану

    """
    _count = 0

    def __init__(self, t, a, b):
        self._x = t.getx()          # _x - координата x точки
        self._y = t.gety()          # _y - координата y точки
        self._a = a                 # - Довжина горизонтальної сторони прямокутника
        self._b = b                 # - Довжина вертикальної сторони прямокутника
        self._visible = False       # _visible - чи є прямокутник видимим на екрані
        self._clr = t.getclr()      # _clr - колір ліній прямокутника
        self._w = t.getw()          # _w - товщина ліній прямокутника
        Priam._count += 1

    def getx(self):
        """Повертає координату x прямокутника

        """
        return self._x

    def gety(self):
        """Повертає координату y прямокутника

        """
        return self._y

    def lengtha(self):
        """Повертає довжину вертикальної сторони a

        """
        return self._a

    def lengthb(self):
        """Повертає довжину горизонтальної сторони b

        """
        return self._b

    def onscreen(self):
        """Перевіряє, чи є прямокутник видимий на екрані

        """
        return self._visible

    def switchon(self):
        """Робить прямокутник видимим на екрані

        """
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.width(self._w)
            turtle.color(self._clr)
            turtle.dot(self._w, self._clr)
            turtle.down()
            turtle.fd(self._b)
            turtle.rt(90)
            turtle.fd(self._a)
            turtle.rt(90)
            turtle.fd(self._b)
            turtle.rt(90)
            turtle.fd(self._a)
            turtle.rt(90)
            turtle.up()

    def switchoff(self):
        """Робить прямокутник невидимим на екрані

        """
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.width(self._w)
            turtle.color(turtle.bgcolor())
            turtle.down()
            turtle.dot(turtle.bgcolor())
            turtle.fd(self._b)
            turtle.rt(90)
            turtle.fd(self._a)
            turtle.rt(90)
            turtle.fd(self._b)
            turtle.rt(90)
            turtle.fd(self._a)
            turtle.rt(90)
            turtle.up()

    def move(self, dx, dy):
        """Пересуває прямокутник на екрані на dx, dy позицій

        """
        vis = self._visible
        if vis:
            self.switchoff()
            self._x += dx
            self._y += dy
            self.switchon()


if __name__ == "__main__":

    turtle.speed(4)
    print("Задана швидкість 4")

    turtle.setup(1000, 800)
    p1 = Point(120, 50, "black", 15)
    p2 = Point(145, -70, "red", 10)
    p3 = Point(-200, -5, "blue")
    pr1 = Priam(p3, 200, 152)
    pr2 = Priam(p2, 100, 255)
    print("Довжина вертикальної сторони першого прямокутика (синього) = {}px".format(pr1.lengtha()))
    print("Довжина горизонтальної сторони першого прямокутика (синього) = {}px".format(pr1.lengthb()))

    p1.switchon()
    p2.switchon()
    pr1.switchon()
    turtle.delay(5)
    pr2.switchon()
    turtle.delay(5)

    pr1.switchoff()
    turtle.delay(20)
    p1.switchoff()
    turtle.delay(5)
    pr2.move(20, -70)
    turtle.delay(20)
    pr2.switchoff()

    turtle.home()
    turtle.mainloop()
