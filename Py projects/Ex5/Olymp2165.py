s = str(input())
previ = s[0]
s1 = ''
for i in s:
    if i == ' ' and previ == ' ':
        continue
    previ = i
    s1 += i
print(s1)

# https://www.e-olymp.com/uk/submissions/9502271
