a = []
d = []

for i in range(2):
    a.append([])
    for j in range(2):
        x = int(input('a[{},{}]='.format(i + 1, j + 1)))
        a[i].append(x)
        d.append(x)

print("Матриця")

for i in range(2):
    print(a[i])

if d[1] == d[2]:
    print("Матриця є симетричною.")
else:
    print("Матриця не є симетричною.")
