n = int(input())
elems = list(map(int, input().split()))
s = ''
for i in range(len(elems)):
    if elems[i] >= 0:
        elems[i] += 2
    s += str(elems[i]) + " "
    s1 = s.rstrip()

print(s1)

# https://www.eolymp.com/uk/submissions/9963500
