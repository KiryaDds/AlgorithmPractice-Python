s = str(input())
m = len(s)

mid = (m + 1) // 2
i = 0
j = 1 - (m % 2)
while mid >= i and mid + j < m:
    if s[mid - i] != s[mid + j]:
        break
    i += 1
    j += 1
print(i)
