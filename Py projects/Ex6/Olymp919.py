n = int(input())
a = list(map(float, input().split()))

amount = 0
suma = 0.00
for i in range(len(a)):
    if a[i] > 0 and (i + 1) % 3 == 0:
        amount += 1
        suma += a[i]
suma = round(suma, 2)
s = str(suma)

for j in range(len(s)):
    if j == len(s) - 3:
        if not(s[j] == "." and s[j + 1].isdigit() and (s[j + 2].isdigit())):
            s += "0"
        elif not(s[j] == ".") and not(s[j + 1].isdigit()) and not(s[j + 2].isdigit()):
            s += ".00"

print(str(amount), s)

# https://www.eolymp.com/uk/submissions/9964260
