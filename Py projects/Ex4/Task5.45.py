n = int(input("n = "))
a0 = float(input("a = "))
index = 1
for i in range(2,  n + 1):
    a = float(input("a = "))
    sub0 = abs(a0 - round(a0))
    subn = abs(a - round(a))
    a0 = a
    if sub0 > subn:
        index = i

print(index)

input()
