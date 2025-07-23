#

"""Модуль, що містить класи для реалізації раціональних дробів.

"""
import sys


class RationalError(ZeroDivisionError):
    """Виключення, яке ініціюється у випадку, коли введено недопустиме значення знаменника дробу ( 0 )."""
    def __init__(self, d):
        self.d = d

    def __str__(self):
        return "Недопустиме значення знаменника дробу: %s ." % self.d


class RationalValueError(Exception):
    """Виключення, яке ініціюється у випадку некоректних даних при застосуванні арифметичних операторів для раціональних
     чисел.
    """
    def __init__(self, something, methodename=''):
        self.something = something
        self.methodename = methodename

    def __str__(self):
        return 'Використано некоректні дані "%s" при застосуванні арифметичного оператору %s!'\
               % (self.something, self.methodename)


class Rational:
    """Клас раціональних дробів

    """

    def __init__(self, num=1, den=1):
        """Конструткор раціонального дробу.
        Якщо знаменник не вказаний або рівний 1, то результат копіюється з
        чисельнику вхідного дробу або строки, яка містить "/". В іншому
        випадку приймається рівно два цілих числа. Якщо знаменник рівний 0,
        то ініціюється відповідна похибка.

        По замовчуванню створюється дріб: "1/1".
        """
        try:
            if den == 0: raise RationalError(den)
            else:
                if isinstance(num, Rational) and den == 1:      # Копіювання
                    self._num = num._num
                    self._den = num._den
                elif isinstance(num, str) and den == 1:         # Рядковий тип
                    num_str, den_str = num.split('/')
                    self._num = int(num_str)
                    self._den = int(den_str)
                elif isinstance(num, int) and isinstance(den, int):     # Чисельний тип
                    self._num = num
                    self._den = den
                else:                                           # Щось інше
                    self._num = int(num)
                    self._den = int(den)

            self.isRational()

        except ValueError:
            print("__init__.Rational: Отримано параметр недопустимого типу або синтаксису! Для рядкового типу потрібно"
                  " заповнювати лише 1-ий параметр у форматі 'n/d'. Для числового типу використовуються тільки цілі"
                  " числа. Для копіювання об'єкту того ж класу використовується тільки перший параметр.")
            exit()
        except:
            print("Несподівана помилка:", sys.exc_info()[0])
            raise

    def gcd(self, m, n):
        """Повертає найбільший спільний дільник для пари (m, n)

        """
        while n != 0:
            m, n = n, m % n
        return m

    def lcm(self, m, n):
        """Повертає найбільше спільне кратне для пари (m, n)

        """
        return (m * n) / self.gcd(m, n)    # (m * n) / m    бо "m" і буде НСД, а тоді вираз спрощується

    def div(self):
        """Скорочення дробу

        """
        if self._den == self._num:
            self._num //= self._num
            self._den //= self._den
        else:
            div = self.gcd(self._num, self._den)
            if self._den // div < 0: div = -div     # Робить знаменник додатнім
            self._num //= div
            self._den //= div

    def isRational(self):
        """Перевіряє, чи це дріб"""
        try:
            self.div()
            if self._num != self._den and self._den != 1 and self._num != 0: return True
            elif self._den == 0: raise RationalError(self._den)
            else: return False
        except ValueError:
            print("Rational.isRational: Отримано параметр недопустимого типу! Для рядкового типу потрібно"
                  " заповнювати лише 1-ий параметр у форматі 'n/d'. Для числового типу використовуються тільки цілі"
                  " числа. Для копіювання об'єкту того ж класу використовується тільки перший параметр.")
            exit()
        except:
            print("Несподівана помилка:", sys.exc_info()[0])
            raise

    def KeyboardInput(self):
        s = input('Введіть дріб у формі "n/d": ')
        return self.StringInput(s)

    def StringInput(self, si):
        s = si
        if "/" in s:
            num_str, den_str = s.split('/')
            num = int(num_str)
            den = int(den_str)
        else:
            c = s.strip()
            i = c.find('.')
            if i >= 0:
                den = 10 ** (len(c) - i - 1)
                num = int(c[:i] + c[i + 1:])
            else:
                num = int(s)
                den = 1

        self._num = num
        self._den = den
        self.isRational()

    def __str__(self):
        """Повертає дріб у виді рядка"""
        if self.isRational(): return str(self._num) + '/' + str(self._den)
        else: return str(self._num)

    def __abs__(self):
        self._num = abs(self._num)
        return self

    def __pos__(self):
        return self.__abs__()

    def __neg__(self):
        self._num = - self._num.__abs__()
        return self

    def __add__(self, other):
        try:
            if isinstance(other, Rational):
                lcm = self.lcm(self._den, other._den)
                res = Rational(self._num * (lcm / self._den) + other._num * (lcm / other._den), lcm)
            elif isinstance(other, int):
                res = Rational(self._num + other * self._den, self._den)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                lcm = self.lcm(self._den, rother._den)
                res = Rational(self._num * (lcm / self._den) + rother._num * (lcm / rother._den), lcm)
            else: raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__add__")

    def __radd__(self, other):
        try:
            if isinstance(other, Rational):
                lcm = self.lcm(self._den, other._den)
                res = Rational(self._num * (lcm / self._den) + other._num * (lcm / other._den), lcm)
            elif isinstance(other, int):
                res = Rational(self._num + other * self._den, self._den)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                lcm = self.lcm(self._den, rother._den)
                res = Rational(self._num * (lcm / self._den) + rother._num * (lcm / rother._den), lcm)
            else: raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__radd__")

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            if isinstance(other, Rational):
                lcm = self.lcm(self._den, other._den)
                res = Rational(self._num * (lcm / self._den) - other._num * (lcm / other._den), lcm)
            elif isinstance(other, int):
                res = Rational(self._num - other * self._den, self._den)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                lcm = self.lcm(self._den, rother._den)
                res = Rational(self._num * (lcm / self._den) - rother._num * (lcm / rother._den), lcm)
            else:
                raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__sub__")

    def __rsub__(self, other):
        try:
            if isinstance(other, Rational):
                lcm = self.lcm(self._den, other._den)
                res = Rational(- self._num * (lcm / self._den) + other._num * (lcm / other._den), lcm)
            elif isinstance(other, int):
                res = Rational(- self._num + other * self._den, self._den)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                lcm = self.lcm(self._den, rother._den)
                res = Rational(- self._num * (lcm / self._den) + rother._num * (lcm / rother._den), lcm)
            else: raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__rsub__")

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        try:
            if isinstance(other, Rational):
                res = Rational(self._num * other._num, self._den * other._den)
            elif isinstance(other, int):
                res = Rational(self._num * other, self._den)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                res = Rational(self._num * rother._num, self._den * rother._den)
            else:
                raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__mul__")

    def __rmul__(self, other):
        try:
            if isinstance(other, Rational):
                res = Rational(self._num * other._num, self._den * other._den)
            elif isinstance(other, int):
                res = Rational(self._num * other, self._den)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                res = Rational(self._num * rother._num, self._den * rother._den)
            else:
                raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__rmul__")

    def __imul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        """Поки воно вміє підносити тільки до цілих степенів"""
        try:
            if isinstance(other, int):
                if other >= 0:
                    res = Rational(self._num ** other, self._den ** other)
                else:
                    res = Rational(self._den ** other, self._num ** other)
            else:
                raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__pow__")

    def __ipow__(self, other):
        return self.__pow__(other)

    def __truediv__(self, other):
        try:
            if isinstance(other, Rational):
                # other = other.__pow__(-1)
                res = Rational(self._num * other._den, self._den * other._num)
            elif isinstance(other, int):
                res = Rational(self._num, self._den * other)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                # rother = rother.__pow__(-1)
                res = Rational(self._num * rother._den, self._den * rother._num)
            else:
                raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__truediv__")

    def __rtruediv__(self, other):
        try:
            if isinstance(other, Rational):
                res = Rational(self._den * other._num, self._num * other._den)
            elif isinstance(other, int):
                res = Rational(self._den * other, self._num)
            elif isinstance(other, float):
                rother = Rational()
                rother.StringInput(str(other))
                res = Rational(self._den * rother._num, self._num * rother._den)
            else:
                raise RationalValueError(other)
            return res
        except RationalError:
            raise RationalValueError(other, "__truediv__")

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __call__(self, item=None):
        return str(float(self._num / self._den))

    def __getitem__(self, item):
        """Квадратні дужки для читання/запису

        """
        if item == "n": return self._num
        elif item == "d": return self._den
        else: pass


if __name__ == "__main__":

    Drib1 = Rational(1, 3)
    Drib2 = Rational()
    s2 = "-5/2"
    Drib2.StringInput(s2)
    Drib3 = Drib1 + Drib2

    Drib4 = Rational(Drib1)
    Drib5 = Drib4 / 3

    print("Дріб створено стандартним чином", Drib1)
    print("Дріб створено із строки", Drib2)
    print("Сума перших двох дробів", Drib3)
    print()
    print("Скопійований з першого дріб", Drib4)
    print("Частка від четвертого дробу та трійки", Drib5)
    print("Дріб 2 по модулю", abs(Drib2))
    print("Дріб 5 (частка) піднесена до 3 степеня", Drib5 ** 3)
    print()
    print("Квадратні дужки ТЕЕЕЕееест (3 дріб, nominator)", Drib3["n"])
    print("Круглі дужки тест (той же дріб)", Drib3())
    print()
    Drib6 = Rational()
    Drib6.KeyboardInput()
    print("Дріб користувача з клавіатури", Drib6)
    print("Від'ємний дріб користувача з клавіатури", -Drib6)
    print("Додатній дріб користувача з клавіатури", +Drib6)

    # DribExceptionTest1 = Rational(3, 0)
    # DribExceptionTest2 = Rational(3, 5)
    # DribExceptionTest2 = DribExceptionTest2 / 0
