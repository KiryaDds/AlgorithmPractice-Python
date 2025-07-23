'''
n = int(input("Row amount = "))
A = []
for i in range(n):
    row = input().split()
    minA = int(row[0])
    for j in range(len(row)):
        if minA > int(row[j]):
            minA = int(row[j])
        # row[j] = int(row[j])
    A.append(minA)
print(A)
'''

n = int(input("Row amount = "))
A = []
for i in range(n):
    row = input().split()
    minA = int(row[0])
    for j in range(len(row)):
        if minA < int(row[j]):
            minA = int(row[j])
        # row[j] = int(row[j])
    A.append(minA)
print(A)