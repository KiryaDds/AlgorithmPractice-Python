n = str(input())

numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in n:
    for j in range(10):
        if i == str(j):
            numbers[j] += 1

s = ""
for i in range(10):
    s += str(numbers[i]) + " "

s = s[0:len(s) - 1]
print(s)

# https://www.eolymp.com/uk/submissions/9979443
