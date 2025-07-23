def zero_one_exchange(s, n):
    res = ''
    res += s[0:n - 1]
    for i in range(n - 1, len(s)):
        if s[i] == "0":
            res += "1"
        elif s[i] == "1":
            res += "0"
        else:
            res += s[i]

    return res


s = input("Введіть рядок з одиницями та нулями: ")
n = int(input("З якого елемента почати перетворення?: "))
print(zero_one_exchange(s, n))
