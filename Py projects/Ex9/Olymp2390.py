def rec_addings(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2] + [1, 1]
    res = []
    for i in range(n, 0, -1):
        lst = [i]
        lst1 = []
        sp1 = rec_addings(n - i)
        for x in rec_addings(n - i)[::-1]:
            lst1 = [i]
            for y in x:



res1 = ""
n = int(input())
v = rec_addings(n)
for i in range(len(v)):
    res1 = res1 + str(v[i]) + " "

res = res1[0:len(res1) - 1]
print(res)

#
