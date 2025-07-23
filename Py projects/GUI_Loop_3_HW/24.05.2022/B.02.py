# B.02

from tkinter import *
from math import sin, cos, tan, radians, pi


class Right_n_angle():

    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.angle = ((self.n-2)*180)/self.n

    def Area(self):
        return self.Perimetre()*self.R_in_Circle()/2

    def Perimetre(self):
        return self.n * self.a

    def R_out_Circle(self):
        return self.a/(2*sin(radians(180/self.n)))

    def R_in_Circle(self):
        return self.a/(2*tan(radians(180/self.n)))

    def draw(self, canv):
        canv.delete("all")
        if canv_window.state() == "iconic":
            canv_window.deiconify()
        x, y = canv_window.winfo_width()//2, canv_window.winfo_height()//2
        r = 500/(2*sin(radians(180/self.n))*self.n)
        coords = [(x + r * cos(2 * pi * i / self.n), y + r * sin(2 * pi * i / self.n)) for i in range(1, self.n+1)]
        for c in range(len(coords)):
            if c == len(coords)-1:
                canv.create_line(coords[-1], coords[0], w=2)
            else:
                canv.create_line(coords[c], coords[c+1], w=2)


def window_processing():
    try:
        fig = Right_n_angle(lis1.get(lis1.curselection()), int(ein1.get()))
        res_l1.configure(text="Отримана фігура: %s-кутник" % fig.n)
        res_l2.configure(text="Радіус вписаного кола: %s (од.)" % fig.R_in_Circle())
        res_l3.configure(text="Радіус описаного кола: %s (од.)" % fig.R_out_Circle())
        res_l4.configure(text="Площа фігури: %s (кв. од.)" % fig.Area())
        res_l5.configure(text="Периметр фігури: %s (од.)" % fig.Perimetre())
        fig.draw(canvas)
    except (TypeError, ValueError):
        err_l.configure(text="Введено недопустиме значення!")
    else:
        err_l.configure(text="")


main_window = Tk()
main_window.title("Створення правильного багатокутника")


sb1 = "Обчислити"
sb2 = "Закрити"
lb1 = len(sb1)
lb2 = len(sb2)
w = max(lb1, lb2) + 2
lis1_info = [3, 4, 5, 6, 7, 8, 10, 12, 18, 20, 30, 40, 50, 100]


f_main = Frame(main_window)
f_main.pack(side=BOTTOM, fill=BOTH, padx=4, pady=4)

b1 = Button(f_main, text=sb1, command=window_processing,
            width=w, height=1,
            bg="white", fg="black",
            font=("Arial", 15, "bold"),
            bd=1, relief=GROOVE)
b1.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

b2 = Button(f_main, text=sb2, command=quit,
            width=w, height=1,
            bg="red", fg="black",
            font=("Arial", 15, "bold"),
            bd=1, relief=GROOVE)
b2.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)


f1_main = Frame(main_window, height=16)
f1_main.pack(side=TOP, fill=BOTH, padx=4, pady=4)


f1_l = LabelFrame(f1_main, text="Виберіть фігуру")
f1_l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

lis1 = Listbox(f1_l, selectmode=BROWSE, height=7)
for i in lis1_info:
    lis1.insert(END, i)
lis1.pack(side=TOP, fill=BOTH, padx=4, pady=4)


f2_l = LabelFrame(f1_main, text="Введіть значення сторони а (од.)")
f2_l.pack(side=RIGHT, fill=BOTH, padx=10, pady=10)

ein1 = Entry(f2_l)
ein1.pack(side=TOP, fill=BOTH, padx=4, pady=4)
err_l = Label(f2_l, text="", fg="red", font=("Arial", 10, "bold"))
err_l.pack(side=TOP, fill=BOTH, padx=4, pady=20)


f3_l = LabelFrame(main_window, text="Результат")
f3_l.pack(side=TOP, fill=BOTH, padx=10, pady=10)

res_l1 = Label(f3_l, text="Отримана фігура: _")
res_l1.pack(side=TOP, fill=BOTH, padx=2, pady=2)
res_l2 = Label(f3_l, text="Радіус вписаного кола: _")
res_l2.pack(side=TOP, fill=BOTH, padx=2, pady=2)
res_l3 = Label(f3_l, text="Радіус описаного кола: _")
res_l3.pack(side=TOP, fill=BOTH, padx=2, pady=2)
res_l4 = Label(f3_l, text="Площа фігури: _")
res_l4.pack(side=TOP, fill=BOTH, padx=2, pady=2)
res_l5 = Label(f3_l, text="Периметр фігури: _")
res_l5.pack(side=TOP, fill=BOTH, padx=2, pady=2)


canv_window = Toplevel()
canv_window.title("Графічне відображення")
canv_window.geometry("500x500")
canv_window.positionfrom()
canv_window.iconify()
canvas = Canvas(canv_window, bg="grey80")
canvas.pack(fill=BOTH, expand=5)


main_window.mainloop()
