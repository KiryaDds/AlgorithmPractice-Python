from collections import namedtuple

Mountain = namedtuple("Mountain", ['name', 'height'])

n = int(input("n = "))
A = []
for i in range(n):
    name = input("Name: ")
    h = int(input("Height: "))
    A.append(Mountain(name, h))

print(A)

maxH = 0
nameM = ""
for x in A:
    if x.height > maxH:
        maxH = x.height
        nameM = x.name

print("Highest mountain is {}".format(nameM))
