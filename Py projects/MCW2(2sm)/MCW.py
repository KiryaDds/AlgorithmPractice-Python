# Основний файл для виконання МКР2

from tkinter import *
from MatrIter import *


def read_f(fn):
    f = open(fn, "r")
    lines = f.readlines()

    A = []
    for line in lines:
        line = list(line.split())
        A.append(line)

    return A


def iterate(obj):
    New_M = MatrIter(obj)
    rezult = ''
    for i in New_M:
        rezult += str(i) + ' '
    lrez.configure(text=rezult)
    #return New_M


def b_hand():
    name = str(ein1.get())
    iterate(read_f(name))


top = Tk()

finput1 = Frame(top)

finput1.pack(fill=X, expand=YES)
Label(finput1, text='Введіть назву файлу: ',
      font=('arial', 16)).pack(side=LEFT)

ein1 = Entry(finput1, font=('arial', 16))
ein1.pack(side=LEFT, fill=X, expand=1)


frez = Frame(top)

frez.pack(fill=X, expand=YES)
lrez = Label(frez,
             text='Результат : ___',
             font=('arial', 16))
lrez.pack(side=LEFT, fill=X)

fbut = Frame(top)
fbut.pack(side=LEFT, fill=X, expand='1')
Button(fbut, text = 'Обчислити',
        command = b_hand,
        bg = "white", fg = "black",
        relief = RAISED,
        font=('arial', 16)).pack(side=LEFT)

Button(fbut, text='Закрити',
        command=top.quit,
        bg = "red", fg = "black",
        relief = GROOVE,
        font=('arial', 16)).pack(side=RIGHT)

top.mainloop()

'''
A = read_f('Matrix for task.txt')
print(A)
A2 = MatrIter(A)
for i in A2:
    print(i)
'''
