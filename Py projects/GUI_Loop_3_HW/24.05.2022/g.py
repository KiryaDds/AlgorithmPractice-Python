from tkinter import *
import math


def sel_handler(ev):
    global fig, n
    nt = lbox.curselection()
    fig = lbox.get(nt)
    n = N[sp.index(fig)]


def printer(event):
    global fig, n
    a = float(av.get())
    t2 = "Помилка вхідних даних: "
    if a <= 0:
        t2 = t2 + "Основа <= 0 !\n"
    else:
        S = math.pi / n
        a2 = a / 2
        R = a2 / math.sin(S)
        r = R * math.cos(S)
        S = a2 * n * r
        t2 = 'ФІГУРА : ' + fig
        t2 = t2 + '\nРадіус описаного кола R={}'.format(R)
        t2 = t2 + '\nРадіус вписаного кола r={}'.format(r)
        t2 = t2 + '\nПлоща ={}'.format(S)

    lb.configure(text=t2)


root = Tk()

sb1 = "Обчислити"
sb2 = "Закрити"
lb1 = len(sb1)
lb2 = len(sb2)
w = max(lb1, lb2) + 2

f1 = Frame(root)
f1.pack(fill=BOTH, padx=4, pady=4)

b1 = Button(f1, text=sb1,
            width=w, height=1,
            bg="white", fg="black",
            font=("Arial", 15, "bold italic"),
            bd=1, relief=RAISED)
b1.bind("<Button-1>", printer)
b1.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

b2 = Button(f1, text=sb2,
            width=w, height=1,
            bg="white", fg="red",
            font=("Arial", 15, "bold italic"),
            bd=1, relief=RAISED,
            command=root.quit)
b2.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)

f2 = Frame(root, height=16)
f2.pack(side=TOP, fill=BOTH, padx=4, pady=4)

f21 = LabelFrame(f2, text="Виберіть правильний багатокутник")
f21.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

n = 3
fig = "Трикутник"
sp = [fig, "Квадрат", "П\'ятикутник", "Шестикутник", "Семикутник",
      "Восьмикутник", "Десятикутник", "Дванадцятикутник", "Вісімнадцятикутник",
      "Двадцятикутник", "Тридцятикутник", "Сорокакутник", "П\'ятидесятикутник",
      "Стокутник"]
N = [3, 4, 5, 6, 7, 8, 10, 12, 18, 20, 30, 40, 50, 100]
svert = Scrollbar(f21)
lbox = Listbox(f21, selectmode=SINGLE, width=20, height=4)
svert.config(command=lbox.yview)
lbox.config(yscrollcommand=svert.set)
svert.pack(side=RIGHT, fill=Y)
lbox.pack(side=LEFT, expand=YES, fill=BOTH)
lbox.delete(0, END)
for esp in sp:
    lbox.insert(END, esp)
lbox.bind('<Double-Button-1>', sel_handler)

f22 = LabelFrame(f2, text="Введіть розмір")
f22.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)

f221 = Frame(f22)
at = Label(f221, text="основа =")
av = Entry(f221)
f221.pack(anchor=NW)
at.pack(side=LEFT)
av.pack(side=LEFT, fill=X, expand=YES)

t3 = "Результат  обчислень"
f3 = LabelFrame(root, text=t3, height=4)
f3.pack(fill=BOTH, padx=4, pady=4)

t2 = " \n "
lb = Label(f3, text=t2)
lb.pack()

root.mainloop()