# Малює перші п'ять фігур

import turtle

turtle.reset()
turtle.speed(4)
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

turtle.rt(90)                                  # Прямокутник
turtle.goto(-320, 260)
turtle.down()
turtle.fd(170)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.fd(170)
turtle.rt(90)
turtle.fd(150)
turtle.rt(90)
turtle.up()

turtle.goto(70, 300)                           # Багатокутник
turtle.down()
turtle.lt(30)
turtle.fd(170)
turtle.rt(20)
turtle.fd(60)
turtle.rt(47)
turtle.fd(90)
turtle.rt(110)
turtle.fd(110)
turtle.rt(30)
turtle.fd(46)
turtle.goto(70, 300)
turtle.up()

turtle.goto(-170, -60)                         # Коло із позначенням центру
turtle.rt(183)
turtle.dot(5, "red")
turtle.write("O")
turtle.bk(60)
turtle.rt(90)
turtle.down()
turtle.circle(60)
turtle.up()

turtle.goto(200, -200)                         # Гриб
turtle.down()
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.circle(60, -180)
turtle.up()
turtle.goto(320, -200)
turtle.down()
turtle.lt(90)
turtle.fd(120)
turtle.end_fill()
turtle.up()
turtle.goto(240, -200)
turtle.lt(90)
turtle.down()
turtle.fd(70)
turtle.lt(90)
turtle.fd(40)
turtle.lt(90)
turtle.fd(70)
turtle.rt(90)
turtle.up()

turtle.home()
turtle.ht()
turtle.mainloop()
