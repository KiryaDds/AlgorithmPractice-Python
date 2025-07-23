n = int(input())
massive = []
for i in range(n):
    massive.append(int(input()))

for i in range(len(massive)//2):
    massive[i], massive[len(massive) - i - 1] = massive[len(massive) - i - 1], massive[i]

s = ""
for i in range(n):
    s += str(massive[i]) + " "

s = s[0:len(s) - 1]
print(s)

# https://www.eolymp.com/uk/submissions/9979203
