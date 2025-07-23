from cmath import exp
while True:
    eps = float(input("eps = "))
    if eps > 0:
        break
    print("Введіть нормальне EPS: ")

z = complex(input("z = "))
t = 1   # z^i/i
i = 0
y = t
while abs(t) > eps:
    i += 1
    t = t * z / i
    y += t

print(y, exp(z))
non_stop = input()
