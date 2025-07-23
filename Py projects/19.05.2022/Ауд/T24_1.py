from tkinter import *


def fun(z, eps=1e-8):
    """Обчислює наближене значення функції f=1/(1+z*z) і n-число членів ряду.
    """

    p = -z * z;
    n = 1;
    a = 1;
    f = 1
    while abs(a) >= eps:
        n += 1;
        a *= p;
        f += a
    return f, n


def calc():
    z = complex(ein1.get())  # отримання значення поля введення
    eps = float(ein2.get())  # отримання значення поля введення

    f, n = fun(z, eps)
    rezult = 'Результат : {}'.format(f)  # побудова рядка для відображення
    lrez.configure(text=rezult)  # зміна надпису значенням результату
    ft = 1 / (1 + z * z)
    rezult = 'Точне знач: {}'.format(ft)  # побудова рядка для відображення
    ltoc.configure(text=rezult)  # зміна надпису значенням результату


top = Tk()  # створення вікна

finput1 = Frame(top)  # контейнер для надпису та поля введення
finput1.pack(fill=X, expand=YES)
Label(finput1, text='Введіть z: ',
      font=('arial', 16)).pack(side=LEFT)  # створення надпису
# та додавання надпису до вікна
ein1 = Entry(finput1, font=('arial', 16))  # створення поля введення
ein1.pack(side=LEFT, fill=X, expand=1)  # додавання поля введення до вікна

finput2 = Frame(top)  # контейнер для надпису та поля введення
finput2.pack(fill=X, expand=YES)
Label(finput2, text='Введіть eps: ',
      font=('arial', 16)).pack(side=LEFT)  # створення надпису
# та додавання надпису до вікна
ein2 = Entry(finput2, font=('arial', 16))  # створення поля введення
ein2.pack(side=LEFT, fill=X, expand=1)  # додавання поля введення до вікна

frez = Frame(top)  # контейнер для надпису результату
frez.pack(fill=X, expand=YES)
lrez = Label(frez,
             text='Результат : ___',
             font=('arial', 16))  # створення надпису
lrez.pack(side=LEFT, fill=X)  # додавання надпису до вікна

ftoc = Frame(top)  # контейнер для надпису результату
ftoc.pack(fill=X, expand=YES)
ltoc = Label(ftoc,
             text='Точне знач: ___',
             font=('arial', 16))  # створення надпису
ltoc.pack(side=LEFT, fill=X)  # додавання надпису до вікна

fbut = Frame(top)  # контейнер для кнопок
fbut.pack(side=LEFT, fill=X, expand='1')
Button(fbut, text='Обчислити',
       command=calc,
       bg="magenta", fg="black",
       relief=RAISED,
       font=('arial', 16)).pack(side=LEFT)  # кнопка "Обчислити"
Button(fbut, text='Закрити',
       command=top.quit,
       bg="yellow", fg="red",
       relief=GROOVE,
       font=('arial', 16)).pack(side=RIGHT)  # кнопка "Закрити"

top.mainloop()