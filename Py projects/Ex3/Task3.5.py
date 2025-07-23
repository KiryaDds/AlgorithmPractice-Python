n = int(input("n = "))
m = int(input("m = "))
if n >= 0 and m >= 0:
    s = 0
    i = 0
    while i < n:
        s = s + m
        i += 1
    print("{}*{}={}".format(m, n, s))
else:
    print("Нас цьому не вчили")
