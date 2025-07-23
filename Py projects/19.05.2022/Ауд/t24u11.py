#  ООП при створенні програми з GUI

from tkinter import *


class But_print:
    def __init__(self):
        sb1 = "Друк тексту"
        sb2 = "Закрити"
        lb1 = len(sb1)
        lb2 = len(sb2)
        w = max(lb1, lb2)

        self.b1 = Button(root, text=sb1,
                         width=w, height=1,
                         bg="white", fg="black",
                         font=("Arial", 15, "bold italic"),
                         bd=4, relief=RAISED)
        self.b1.bind("<Button-1>", self.printer)
        self.b1.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

        self.b2 = Button(root, text=sb2,
                         width=w, height=1,
                         bg="yellow", fg="red",
                         font=("Verdana", 15, "bold"),
                         bd=4, relief=GROOVE,
                         command=root.quit)
        self.b2.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)

    def printer(self, event):
        print("Уже надрукував !!")


root = Tk()
obj = But_print()
root.mainloop()