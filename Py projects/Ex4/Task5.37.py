from math import sqrt
x = float(input())

while True:
    EPS = float(input("EPS = "))
    if EPS > 0:
        break
    print("Введіть нормальне EPS: ")

t = sqrt(0.5)
p = t
p_prev = 0
while abs(p - p_prev) > EPS:
    p_prev = p
    t = sqrt(0.5 + 0.5 * t)
    p *= t

print(p, 2 / p)
non_stop = input()
