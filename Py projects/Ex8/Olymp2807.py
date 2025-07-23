n = int(input())
s = input()
d = {}

for i in range(len(s)):
    if s[i] not in d.keys():
        d[s[i]] = 1
    else:
        val = d[s[i]]
        del d[s[i]]
        d[s[i]] = val + 1


flag = 0
for i in d.keys():
    if d.get(i) == min(d.values()):
        flag = 1
        print(i)
        break
    else:
        flag = 0

if flag == 0:
    print("Ok")

'''n = int(input())
s = input()
d = {}

for i in range(len(s)):
    if s[i] not in d.keys():
        d[s[i]] = 1
    else:
        d[s[i]] = 2

flag = 0
for i in d.keys():
    if d.get(i) == 1:
        flag = 1
        print(i)
        break
    else:
        flag = 0

if flag == 0:
    print("Ok")'''

# https://www.eolymp.com/uk/submissions/9981616 - 35%
