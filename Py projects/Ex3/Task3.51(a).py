n = int(input("n = "))
y = float(input("Введіть перше дійсне 'y': "))
if abs(y) <= 2:
    maxz = y
else:
    maxz = 0.5

for i in range(1, n):
    y = float(input("y = "))
    if abs(y) <= 2:
        z = y
    else:
        z = 0.5
    if maxz < abs(z):
        maxz = z
print("max = ", maxz)

non_stop = input()
