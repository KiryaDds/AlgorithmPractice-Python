'''
n = int(input())

S = {0: 0, 1: 2, 20: 30, 100: 100}


def min_sum(m):
    n = 2
    while n <= m:
        m2 = m3 = 100000000000
        m1 = S[n - 1] + 2
        if n >= 20:
            m2 = S[n - 20] + 30
        if n >= 100:
            m3 = S[n - 100] + 100
        S[n] = min(m1, m2, m3)
        n += 1
    return S[m]


print(min_sum(n))
'''

n = int(input())

sumn = 0
n1 = 0
n10 = 0
n100 = n // 100
if n100 != 0:
    sumn += 100 * n100
    n10 = (n - 100*n100) // 20
    if n10 != 0:
        sumn += 30 * n10
        n1 = n - 100*n100 - 20*n10
        sumn += 2 * n1
    else:
        n1 = n - 100 * n100
        sumn += 2 * n1
else:
    n10 = n // 20
    if n10 != 0:
        sumn += 30 * n10
        n1 = n - 100*n100 - 20*n10
        sumn += 2 * n1
    else:
        n1 = n - 100 * n100
        sumn += 2 * n1

print(sumn)


# print(n100)
# print(n10)
# print(n1)

# https://www.eolymp.com/ru/submissions/9962115 - 46%
