#  Типова схема (сценарій) створення програми з GUI

# 1. Імпорт бібліотеки
from tkinter import *

# 1.1. Розміщення функцій для обробки подій (за наявності)
def printer(event):
     print ("Уже надрукував !!")

# 2. Створення головного вікна
root = Tk()

# 3. Створення графічних об'єктів = віджет ("штучок")
b1 = Button(root)

# 4. Встановлення властивостей віджет
sb1 = "Друк тексту"
sb2 = "Закрити"
lb1 = len(sb1)
lb2 = len(sb2)
w = max(lb1, lb2)
b1['text'] = sb1                             # напис на кнопці
b1['width'] = w                              # ширина (в символах)
b1['height'] = 1                             # висота
b1['bg'] = "white"                           # колір фону - yellow|magenta|cyan|red|green|blue|white|black
b1['fg'] = "black"                           # колір надпису
b1['font'] = ("Arial",15,"bold italic")      # шрифт - (<назва>,<розмір>,<написання>)
                                                        # <назва>     - Verdana
                                                        # <розмір>    - 12
                                                        # <написання> - bold|italic|bold italic|normal
                                       #  виділення віджета :
b1['bd'] = 4                                 # ширина границі (в символах)
b1['relief'] = RAISED                        # <рельєф>  - FLAT|SUNKEN|RAISED|GROOVE|RIDGE|SOLID

# 5-6. Означення подій та імен функцій обробників цих подій
b1.bind("<Button-1>",printer)                # викликається функція <printer> та їй передається в якості
                                             # параметру об’єкт event, що містить характеристики події

# 7. Розміщення віджет з допомогою менеджерів розміщення
#       pack   - пакувальник, розміщує елемент за положенням
#       grid   - таблиця, розміщує елементи як у таблиці
#       place  - розміщення по заданих позиціях
b1.pack(side=LEFT, fill=BOTH, padx=4, pady=4)

b2 = Button(root,text = sb2,
            width = w, height = 1,
            bg = "yellow", fg = "red",
            font = ("Verdana",15,"bold"),
            bd = 4, relief = GROOVE, command=root.quit)

b2.pack(side=RIGHT, fill=BOTH, padx=4, pady=4)

# 8. Відображення головного вікна
root.mainloop()