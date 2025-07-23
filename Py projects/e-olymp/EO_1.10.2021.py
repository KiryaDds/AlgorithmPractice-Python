n = int(input())
a = 0
sums = 0
while a < n:
    if a % 2 == 0:
        x = a
        sums += x
    a += 1
print(sums)
