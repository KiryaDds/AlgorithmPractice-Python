s = str(input("Введіть строку: "))
s_mono = ""
for i in range(0, len(s)):
    if i == len(s) - 1:
        if ord(s[i - 1]) + 1 == ord(s[i]):
            s_mono += s[i]
        break
    else:
        if ord(s[i]) + 1 == ord(s[i + 1]):
            s_mono += s[i]

# print(s_mono)

s_length = ""
u = 0
flag = 0
for j in range(u, len(s_mono)):
    if j == len(s_mono) - 1:
        if ord(s_mono[j - 1]) > ord(s_mono[j]):
            u = j + 1
            s_length = s_mono[u:j]
            if flag == 0:
                flag = 1
                s_length2 = s_length
            if len(s_length) < len(s_length2):
                s_length = s_length2
        break
    else:
        if ord(s_mono[j]) > ord(s_mono[j + 1]):
            u = j + 1
            s_length = s_mono[u:j]
            if flag == 0:
                flag = 1
                s_length2 = s_length
            if len(s_length) < len(s_length2):
                s_length = s_length2
if flag == 1:
    print(s_length)
else:
    print("Таких підрядків не знайдено!")


# print(ord("a"))
# print(ord("b"))
# print(ord("c"))
