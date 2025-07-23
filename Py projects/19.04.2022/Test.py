# Файл обчислення значення суми Sn на основі раціональних дробів з класу Rational

from Rational import *

Sn = Rational(); n = int(input("n = "))
for i in range(1, n): Sn += Rational((-1)**i * i, i + 1)
print("Сума = ", Sn()); print("Сума = ", Sn)
