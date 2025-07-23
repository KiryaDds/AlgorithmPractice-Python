n = int(input())
il = map(int, input().split())

z = {}
for x in il:
    if x in z:
        z[x] += 1
    else:
        z[x] = 1

res = -1
for k, v in z.items():
    if z[k] > n//2:
        res = k

print(res)

# https://www.eolymp.com/uk/submissions/9981500
