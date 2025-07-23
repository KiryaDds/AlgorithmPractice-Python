s = str(input())
big_ord = ord(s[0])
big = s[0]
for x in s:
    if ord(x) > big_ord:
        big_ord = ord(x)
        big = str(x)

amount = s.count(big)
print(big, " ", amount)


