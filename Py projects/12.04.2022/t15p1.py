# t15p1.py
#    Приклади обробка помилок та виключних ситуацій.

print("Пр.1    Захищене введення інформації")
while True:
    try:
        n = int(input("Введіть n>=0 :"))
        if n > -1: break
        else:
            print("Число <0 !")
    except ValueError:
        print("Введена інформація НЕ ЦІЛЕ число! Спробуйте знову...")
print("n=",n)


print("\nПр.2    Обробка можливих помилок при роботі з файлом")
'''   В рядках текстового файла записана деяка інформація.
      Знайти суму цілих чисел.
'''
import sys


try:
    s = None
    f = open('t15p1.txt')
    while True :
        try :
            c = f.readline();  c.strip()
            if len(c) == 0: break
            if s == None: s = 0
            i = int(c)
            s += i
        except EOFError:
            break
        except ValueError:
            #print("Неможливо конвертувати дані в ціле число.")
            continue
    f.close()
except FileNotFoundError as fn:
    print("Файл не знайдено:", fn.filename)
except OSError as e:
    print("Помилка ОС")
    raise e
except IOError as err:
    print("Помилка вводу/виводу (%s): %s" % (err.errno, err.strerror))
except:
    print("Несподівана помилка:", sys.exc_info()[0])
    raise
else:
    pass
finally:
    print("Сума цілих у файлі=", s)


print("\nПр.3    Ініціювання виключень")
'''  Т15.4. Скласти функцію зі змінною кількістю параметрів для обчислення
     f(x1,...,xn,y1,...,yn)=Σ(x[i]**2+y[i]**2+x[i]*y[i]).
'''


def square_sum(*ar, **kw):
    try:
        if len(ar) != len(kw):
            raise ValueError("Не співпадає кількість позиційних і ключових параметрів")
        else:
            sum = 0
            for x, y in zip(ar, kw.values()):
                sum += x**2 + y**2 + x*y
    except ValueError:
        sum = None
    return sum


print(square_sum(1, -2, 4, y1=2, y3=3, y2=3))
print(square_sum(1, 4, y1=2, y3=3, y2=3))


print('\nПр.4     "Швидке" обчислення x**n')


def swiftpow(x, n):
    """Використання інваріанта z*t**k == x**n.

    """
    z = 1;  t = x;  k = n
    while k > 0:
        if k % 2 == 0:
            t = t * t;  k //= 2
        else:
            z *= t;  k -= 1
    try:
        xn = x**n
        assert z == xn, str(z)+', '+str(xn)
    except AssertionError :
        if abs(z - xn) >= 1e-16 :
            print("swiftpow(%f,%d): Абсолютна похибка перевищила 1е-16" % (x, n))
    return z


x = 1.5;  n = 27;  y = swiftpow(x, n)
print('%f**%d =' % (x, n), y)

x = 12.4;  n = 17;  y = swiftpow(x, n)
print('%f**%d =' % (x, n), y)
