a = str(input())
splited_4 = []
res = ""
while len(a) % 4 != 0:
    a = "0" + a

for i in range(1, len(a)//4 + 1):
    splited_4.append(a[4 * (i - 1): 4 * i])

for j in range(len(splited_4)):
    k = 1
    n = 0
    s = str(splited_4[j])
    s_reverse = s[3] + s[2] + s[1] + s[0]
    for g in s_reverse:
        n += int(g)*k
        k *= 2
    if n == 10:
        res += "A"
    elif n == 11:
        res += "B"
    elif n == 12:
        res += "C"
    elif n == 13:
        res += "D"
    elif n == 14:
        res += "E"
    elif n == 15:
        res += "F"
    else:
        res += str(n)
res = res.lstrip("0")
print(res)

# https://www.eolymp.com/uk/submissions/9963049
