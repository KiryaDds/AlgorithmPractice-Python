n = int(input())
sumn = 0
if n <= 1000:
    n1 = n % 20
    n10 = int((n % 100) / 20)
    sumn = int(n / 100) * 100 + n10 * 30 + n1 * 2
    if n < 100:
        n1 = n % 20
        sumn = int(n / 20) * 30 + n1 * 2
        if n < 20:
            sumn = n * 2
print(sumn)

'''
n = int(input())
sumn = 0
if n <= 1000:
    n1 = n % 20
    n10 = (n % 100) // 20
    sumn = (n // 100) * 100 + n10 * 30 + n1 * 2
    if n < 100:
        n1 = n % 20
        sumn = (n // 20) * 30 + n1 * 2
        if n < 20:
            sumn = n * 2 
print("sum = ", sumn)
'''