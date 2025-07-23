# Малює "Хрест". Параметр "а" знаходиться у 38 строці

import turtle
import math

turtle.reset()
turtle.speed(0)
turtle.width()
turtle.setup(1040, 1040, 480, 0)
turtle.up()

turtle.goto(-480, 0)                    # Малює координатні осі з розмірністю у пікселях
turtle.pd()
for i in range(-4, 5):
    if i != 4:
        turtle.write(str(120 * i))
        turtle.dot(3)
        turtle.fd(120)
    else:
        turtle.write("X", False, "right", font=("Verdana", 12, "bold"))
turtle.pu()

turtle.goto(0, -480)
turtle.lt(90)

turtle.pd()
for i in range(-4, 5):
    if i != 4:
        turtle.write(str(120 * i))
        turtle.dot(3)
        turtle.fd(120)
    else:
        turtle.write("Y", False, "left", font=("Verdana", 12, "bold"))
turtle.pu()

turtle.width(2)

a = 60                     # Параметр а

for phi in range(-180, 181):            # Малює хрест
    if phi == 0 or phi % 180 == 0:      # Прибирає зайві лінії та помилки
        turtle.up()
        continue
    phi = math.radians(phi)
    p = (2*a)/math.sin(2*phi)
    x = p*math.cos(phi)
    y = p*math.sin(phi)
    turtle.goto(x, y)
    turtle.down()

turtle.up()

for phi in range(180, -181, -1):        # Повторення у зворотному порядку для отримання більш цільного малюнку
    if phi == 0 or phi % 180 == 0:
        turtle.up()
        continue
    phi = math.radians(phi)
    p = (2*a)/math.sin(2*phi)
    x = p*math.cos(phi)
    y = p*math.sin(phi)
    turtle.goto(x, y)
    turtle.down()

turtle.up()
turtle.home()
turtle.ht()
turtle.mainloop()
