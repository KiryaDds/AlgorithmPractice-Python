s = str(input())
previ = s[0]
s1 = s[0]
for i in s:
    if i == previ:
        continue
    previ = i
    s1 += i
print(s1)

# https://www.e-olymp.com/uk/submissions/9502292
