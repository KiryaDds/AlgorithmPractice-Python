n = int(input("n = "))
a = n
k = 0
while a > 0:
    c = a % 10
    k = 10 * k + c
    a = a // 10
if k == n:
    print("Паліндром")
else:
    print("Не паліндром")
non_stop = input()
