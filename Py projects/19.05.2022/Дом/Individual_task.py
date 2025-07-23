from tkinter import *
from math import cosh


def fun(z, eps=1e-8):
    """Обчислює наближене значення функції №14 f=ch(z) і n-число членів ряду.
    """

    def Gfun(z):
        n = 1; p = z*z/(n*n+n); a = 1; f = 1
        yield f, a, n
        while True:
            n += 1; a *= p; f += a
            yield f, a, n

    try:
        z = complex(z); eps = float(eps)
        if 0 < eps < 1 and abs(z) < 1:
            e = eps
            for f, a, n in Gfun(z):
                if abs(a) <= e: break
            return f, n
        else:
            raise ValueError

    except Exception:
        try:
            rezult = 'Результат : Введено недопустиме значення %s = %s' % \
                     ('z' if abs(z) >= 1 else "eps", z if abs(z) >= 1 else eps)
            lrez.configure(text=rezult)
            rezult = 'Допустимі значення : z є (-1-0j; 1+0j), eps є (0; 1)'
            ltoc.configure(text=rezult)
        except TypeError:
            rezult = 'Результат : Введено недопустиме значення z = %s' % z
            lrez.configure(text=rezult)
            rezult = 'Допустимі значення : z є (-1-0j; 1+0j), eps є (0; 1)'
            ltoc.configure(text=rezult)


def calc():
    z = ein1.get()
    eps = ein2.get()

    f, n = fun(z, eps)
    rezult = 'Результат : %s . Використано доданків: %s' % (f, n)
    lrez.configure(text=rezult)

top = Tk()

finput1 = Frame(top)
finput1.pack(fill=X, expand=YES)
Label(finput1, text='Обчислення наближеного значення функції №14 f=ch(z) і n-числа членів ряду.',
      font=('arial', 16)).pack(side=TOP)
Label(finput1, text='Введіть z: ',
      font=('arial', 16)).pack(side=LEFT)

ein1 = Entry(finput1, font=('arial', 16))
ein1.pack(side=LEFT, fill=X, expand=1)

finput2 = Frame(top)
finput2.pack(fill=X, expand=YES)
Label(finput2, text='Введіть eps: ',
      font=('arial', 16)).pack(side=LEFT)

ein2 = Entry(finput2, font=('arial', 16))
ein2.pack(side=LEFT, fill=X, expand=1)

frez = Frame(top)
frez.pack(fill=X, expand=YES)
lrez = Label(frez,
             text='Результат : ___',
             font=('arial', 16))
lrez.pack(side=LEFT, fill=X)

ftoc = Frame(top)
ftoc.pack(fill=X, expand=YES)
ltoc = Label(ftoc,
             text='',
             font=('arial', 16))
ltoc.pack(side=LEFT, fill=X)

fbut = Frame(top)  # контейнер для кнопок
fbut.pack(side=LEFT, fill=X, expand='1')
Button(fbut, text='Обчислити',
       command=calc,
       bg="white", fg="black",
       relief=GROOVE,
       font=('arial', 16)).pack(side=LEFT)
Button(fbut, text='Закрити',
       command=top.quit,
       bg="red", fg="black",
       relief=GROOVE,
       font=('arial', 16)).pack(side=RIGHT)

top.mainloop()
