# n = int(input())
# amount = ((10**n - 1) - (10**(n - 1))) # - (((10**n - 1) // 6) - (10**(n - 1) // 6))
# print(amount)


n = int(input())

s = ''
for i in range(10**(n - 1), 10**n):
    s += str(i)
amount = (10**n - 1) - 10**(n - 1) - s.count('6')
print(amount)

# Все хуйня, давай по новой