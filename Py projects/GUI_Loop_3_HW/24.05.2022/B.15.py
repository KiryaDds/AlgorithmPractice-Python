# B.15

from tkinter import *


def Binom_fun(a, b, n):
    C = 1; an = 1; bn = 1; fn = n
    for i in range(1, n+1):
        an *= a
    S = C*an*bn; s = '(a + b)^n = ' + str(int(S)) + ' + '
    for i in range(1, n+1):
        an /= a; bn *= b; C *= fn/i; fn -= 1; S += C*an*bn; s += str(int(S)) + ' + '
    s = s.rstrip(' + ')
    return S, s


def window_processing():
    try:
        S, s = Binom_fun(int(ein1.get()), scl1.get(), lis1.get(lis1.curselection()))
        res_l1.configure(text="Отримане значення, обчислене «в лоб»: %s" %
                              (int(ein1.get()) + scl1.get())**lis1.get(lis1.curselection()))
        res_l2.configure(text="Отримане значення, обчислене по рекурентній формулі «розкладу»: %s " % int(S))

        if result_window.state() == "iconic":
            result_window.deiconify()
        res_t3.delete('1.0', END)
        ls = len(s)
        k = 0
        step = 50
        for x in range(0, ls, step):
            if x+step < ls:
                s = s[x:x+step]
                res_t3.insert(str(x)+'.'+str(k), s)
            else:
                s = s[x:]
                res_t3.insert(str(x)+'.'+str(k), s)
                break
            k += 1

    except (TypeError, ValueError):
        err_l.configure(text="Введено недопустиме значення!")
    else:
        err_l.configure(text="")


def finish():
    if finish_dialog_window.state() == "iconic":
        finish_dialog_window.deiconify()


def finish_cancel():
    if finish_dialog_window.state() != "iconic":
        finish_dialog_window.iconify()


main_window = Tk()
main_window.title("Обчислення (a + b)^n, a є R, b є Q(ціле), n>1")


sb1 = "Обчислити"
sb2 = "Закінчити роботу"
lb1 = len(sb1)
lb2 = len(sb2)
w = max(lb1, lb2) + 2
lis1_info = [x for x in range(2, 9)]


f_main = Frame(main_window)
f_main.pack(side=BOTTOM, fill=BOTH, padx=4, pady=4)

b1 = Button(f_main, text=sb1, command=window_processing,
            width=w, height=1,
            bg="white", fg="black",
            font=("Arial", 15, "bold"),
            bd=1, relief=GROOVE)
b1.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

b2 = Button(f_main, text=sb2, command=finish,
            width=w, height=1,
            bg="red", fg="black",
            font=("Arial", 15, "bold"),
            bd=1, relief=GROOVE)
b2.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)


f1_main = Frame(main_window, height=16)
f1_main.pack(side=TOP, fill=BOTH, padx=4, pady=4)


f1_l = LabelFrame(f1_main, text="Оберіть n :")
f1_l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

lis1 = Listbox(f1_l, selectmode=BROWSE, height=7)
for i in lis1_info:
    lis1.insert(END, i)
lis1.pack(side=TOP, fill=BOTH, padx=4, pady=4)


f2_l = LabelFrame(f1_main, text="Введіть а ")
f2_l.pack(side=TOP, fill=BOTH, padx=10, pady=10)

ein1 = Entry(f2_l)
ein1.pack(side=TOP, fill=BOTH, padx=4, pady=4)
err_l = Label(f2_l, text="", fg="red", font=("Arial", 10, "bold"))
err_l.pack(side=TOP, fill=BOTH, padx=4, pady=20)
scl1 = Scale(f2_l, from_=-30, to=30, tickinterval=5, resolution=10,
             label="Оберіть b :", orient=HORIZONTAL, length=125)
scl1.pack(side=TOP, fill=X, padx=4, pady=4)


f3_l = LabelFrame(main_window, text="Результат")
f3_l.pack(side=TOP, fill=BOTH, padx=10, pady=10)

res_l1 = Label(f3_l, text="Отримане значення, обчислене «в лоб»: _")
res_l1.pack(side=TOP, fill=BOTH, padx=2, pady=2)
res_l2 = Label(f3_l, text="Отримане значення, обчислене по рекурентній формулі «розкладу»: _")
res_l2.pack(side=TOP, fill=BOTH, padx=2, pady=2)


result_window = Toplevel()
result_window.title("Рядок тексту з розкладом")
result_window.iconify()

res_t3 = Text(result_window)
res_t3.pack(side=TOP, fill=BOTH, padx=2, pady=2)


finish_dialog_window = Tk()
finish_dialog_window.title("Закінчення роботи")
finish_dialog_window.iconify()

Label(finish_dialog_window, text="Чи ви дійсно бажаєте закінчити роботу?",
      font=("Arial", 16, "bold")).pack(side=TOP, fill=BOTH, padx=4, pady=20)
b_yes = Button(finish_dialog_window,
               text="Так", command=quit,
               width=w, height=1,
               bg="red", fg="black",
               font=("Arial", 15, "bold"),
               bd=1, relief=RAISED)
b_yes.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

b_no = Button(finish_dialog_window,
              text="Ні", command=finish_cancel,
              width=w, height=1,
              bg="green", fg="black",
              font=("Arial", 15, "bold"),
              bd=1, relief=RAISED)
b_no.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)


main_window.mainloop()
