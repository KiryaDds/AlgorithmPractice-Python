def to_int(x):
    return int(x, 2)


def to_bin(x):
    res = ""
    while x > 0:
        d = x % 2
        x //= 2
        res += str(d)
    return res[::-1]


def sumn(x, y):
    return x + y


A = input()
B = input()
z = str(to_bin(sumn(to_int(A), to_int(B))))
print(z)

# https://www.eolymp.com/uk/submissions/9980147 - 95%
