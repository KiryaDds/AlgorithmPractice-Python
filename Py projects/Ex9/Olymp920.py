def min(x, y):
    return x if x < y else y


def max(x, y):
    return y if x < y else x


def min3(a, b, c):
    return min(min(a, b), c)


x, y, z = map(float, input().split())

print(min3(max(x, y), max(y, z), x + y + z))

# https://www.eolymp.com/uk/submissions/10028166
