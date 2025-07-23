from tkinter import *
from math import *

n=int(input('Введите n: '))
t=0
o=0
l=[]
s=[]
g=0
x_max=0
y_max=0
x_min=0
y_min=0
count=0


def tochki():
    global o
    global t  # глобальные переменные
    global l
    global x_min
    global y_min
    global x_max
    global y_max
    for i in range (n):
        x=float(input('Введите x: '))
        y = float(input('Введите y: '))
        l.append(x)
        l.append(y)
    x_max=l[0]
    y_max=l[1]
    y_min=l[1]
    x_min=l[0]
    i=0
    while (i<2*n):
        if(x_max<l[i]):
            x_max=l[i]
        i=i+2
    i=1
    while(i<2*n):
        if(y_max<l[i]):
            y_max=l[i]
        i=i+2
    i=0
    while i<2*n:
        if (x_min>l[i]):
            x_min=l[i]
        i=i+2
    i=1
    while i<2*n:
        if (y_min>l[i]):
            y_min=l[i]
        i=i+2
    if miny<0:
        t=y_min
    if minx<0:
        o=x_min


def plocha():
    i=0
    j=0
    u=0
    global n
    global count
    global s
    while i<=(2*n-1):
        j=0
        while j<=(2*n-1):
            u=0
            if (i==j):
                j=j+2
                continue
            while u<=(2*n-1):
                if(u==j or u==i):
                    u=u+2
                    continue
                if ((l[j] - l[i]) * (l[u+1] - l[i+1]) - (l[u] - l[i]) * (l[j+1] - l[i+1]))!=0:
                    a=sqrt((l[j]-l[i])**2+(l[j+1]-l[i+1])**2)
                    b=sqrt((l[u]-l[i])**2+(l[u+1]-l[i+1])**2)
                    c=sqrt((l[j]-l[u])**2+(l[u+1]-l[j+1])**2)
                    p=(a+b+c)/2
                    s.append(sqrt(p*(p-a)*(p-b)*(p-c)))
                    count=count+1
                u=u+2
            j=j+2
        i=i+2


def maxplocha():
    global g1
    global g2  # глобальные переменные
    global g3
    i=0
    l1=[]
    j=0
    maxs=s[0]
    while (i<count):
        if(maxs<=s[i]):
            maxs=s[i]
        i=i+1
    i=0
    j=0
    u=0
    while i<=(2*n-1):
        j=0
        while j<=(2*n-1):
            u=0
            if (i==j):
                j=j+2
                continue
            while u<=(2*n-1):
                if(u==j or u==i):
                    u=u+2
                    continue
                if ((l[j] - l[i]) * (l[u+1] - l[i+1]) - (l[u] - l[i]) * (l[j+1] - l[i+1]))!=0:
                    a=sqrt((l[j]-l[i])**2+(l[j+1]-l[i+1])**2)
                    b=sqrt((l[u]-l[i])**2+(l[u+1]-l[i+1])**2)
                    c=sqrt((l[j]-l[u])**2+(l[u+1]-l[j+1])**2)
                    p=(a+b+c)/2
                if (maxs==sqrt(p*(p-a)*(p-b)*(p-c))):
                    g1=i
                    g2=j
                    g3=u
                    break
                u=u+2
            j=j+2
        i=i+2


def paint():
    pol=Tk()
    canvas= Canvas (pol, width=(maxx-o)*100, height=(maxy-t)*100)
    canvas.pack()
    canvas.create_polygon((l[g1]-o)*50, (l[g1+1]- t)*50, (l[g2]-o)*50, (l[g2+1]-t)*50, (l[g3]-o)*50, (l[g3+1]-t)*50)
    pol.mainloop()


def circle():       # рисуем треугольник
    r=sqrt((maxx-minx)**2+(maxy-miny)**2)/2
    i=0
    yo=0
    xo=0
    print (maxy, maxx)
    while (i<n*2):
        if(i%2==0):
            xo=+(l[i]/n)
        else:
            yo=+(l[i]/n)
        i=i+1
    print('Круг с центром в точке', '(', xo, ';', yo, ')', 'С радиусом', r)


tochki()
plocha()
maxplocha()
paint()
circle()
