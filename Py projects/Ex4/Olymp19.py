N = str(input())

grad = 0
if len(N) % 2 == 0:
    for i in range(0, len(N)//2):
        if N[i] == N[-i-1]:
            grad += 1

else:
    grad += 1
    for i in range(0, (len(N) - 1)//2):
        if N[i] == N[-i-1]:
            grad += 1

print(grad)

# https://www.eolymp.com/uk/submissions/9961777
