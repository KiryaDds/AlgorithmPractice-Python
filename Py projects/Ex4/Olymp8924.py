n = str(input())
sum_doubles = 0
flag = 0
for i in n:
    if int(i) % 2 == 0:
        sum_doubles += int(i)
        flag = 1
if sum_doubles == 0 and flag == 0:
    print(-1)
else:
    print(sum_doubles)

# https://www.eolymp.com/uk/submissions/9961854
