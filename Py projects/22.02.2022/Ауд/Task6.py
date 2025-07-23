# Малює лемніскату Бернуллі. Параметр "а" знаходиться у 38 строці

import turtle
import math

turtle.reset()
turtle.speed(0)
turtle.width()
turtle.setup(1040, 1040, 440, 0)
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

a = 170                     # Параметр а

for phi in range(0, 181):               # Малює праву частину лемніскати
    phi = math.radians(phi)
    p = math.sqrt(abs(math.tan(math.pi/4 - phi)))
    x = a*math.sqrt(2)*((p+p**3)/(1+p**4))
    y = a*math.sqrt(2)*((p-p**3)/(1+p**4))
    turtle.goto(x, y)
    turtle.down()

turtle.up()
for phi in range(0, 181):               # Малює ліву частину лемніскати
    phi = math.radians(phi)
    p = -math.sqrt(abs(math.tan(math.pi / 4 - phi)))
    x = a * math.sqrt(2) * ((p + p ** 3) / (1 + p ** 4))
    y = a * math.sqrt(2) * ((p - p ** 3) / (1 + p ** 4))
    turtle.goto(x, y)
    turtle.down()

turtle.up()
turtle.home()
turtle.ht()
turtle.mainloop()
