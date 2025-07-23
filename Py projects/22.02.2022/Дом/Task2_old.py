# Програма візуалізації системи прямокутників та її переміщення

from Task1 import Point, Priam
import turtle

f1_name = "t13z10.1"
f2_name = "t13z10.2"
f3_name = "t13z10.4"
f4_name = "t13z10.8"
task = -1
while True:
    print("\n", f1_name, "\n",
          f2_name, "\n",
          f3_name, "\n",
          f4_name, "\n",)
    task = input("Оберіть файл для виконання серед наведених вище або закінчити виконання 'stop' або '0': ")
    if task == "0" or task == "stop":
        break
    s = []
    prl = []
    f = open(task.strip(), "r")
    lines = f.readlines()
    for line in lines:
        s.append(list(map(str, line.split())))
    for j in s:
        p = Point(int(j[0]), int(j[1]), j[2], int(j[3]))
        pr = Priam(p, int(j[4]), int(j[5]))
        prl.append(pr)
    turtle.speed(0)
    turtle.setup(1000, 1000)
    turtle.ht()
    while True:
        for i in prl:
            i.switchon()
            i.move(70, -70)

        for i in prl:
            i.switchon()
            i.move(-70, -70)

        for i in prl:
            i.switchon()
            i.move(-70, 70)

        for i in prl:
            i.switchon()
            i.move(70, 70)
