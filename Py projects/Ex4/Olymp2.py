n = int(input())
i = 0
if n == 0:
    i = 1
else:
    while n >= 1:
        n = n / 10
        i += 1
print(i)

# https://www.e-olymp.com/uk/submissions/9734579
