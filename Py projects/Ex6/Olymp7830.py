s = input()
sp = s.split()
a = []
for x in sp:
    a.append(int(x))

'''
max_x = a[0]
for i in range(1, len(a)):
    if max_x < a[i]:
        max_x = a[i]
'''

lst_ints = [int(x) for x in input().split()]

max_x = lst_ints[0]
for x in lst_ints[1:]:
    if max_x < x:
        max_x = x

print(max(lst_ints))

# https://www.e-olymp.com/uk/submissions/9616418
