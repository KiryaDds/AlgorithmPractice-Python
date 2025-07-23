z = float(input("z = "))
n = 0
a0 = 0
EPS = 0.0000001
while True:
    arctg_z = a0 + (-1)**n * (z**(2 * n + 1) / (2 * n + 1))
    if abs(arctg_z - a0) < EPS:
        break
    n += 1
    a0 = arctg_z
print("Сума дорівнює: ", arctg_z)
input()
