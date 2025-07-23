x = float(input("x = "))

while True:
    EPS = float(input("EPS = "))
    if EPS > 0:
        break
    print("Введіть нормальне EPS: ")

a = x   # (-1)^i x^(2i + 1)/(2i + 1)i!
y = x   # Intergal
i = 0
while abs(a) > EPS:
    i += 1
    a = a * (-x**2) / i * (2 * i - 1) / (2 * i + 1)
    y += x
print("y = {}".format(y))

non_stop = input()
