s1 = ""
s = input("Введіть рядок з повторюванними символами: ")
listed = [x for x in s]
for i in s:
    k = s.count(i)
    while k > 1:
        a = s.rfind(i)
        listed[a] = ""
        k -= 1

res = ""
for i in range(len(listed)):
    res += str(listed[i])

print(res)
