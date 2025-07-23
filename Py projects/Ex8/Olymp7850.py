n = int(input())
il = [int(x) for x in input().split()]

counts = {}
index_memory = {}

for i, x in enumerate(il):
    if x in counts:
        counts[x] += 1
        index_memory[x] = i
    else:
        counts[x] = 1
        # index_memory[x] = i

if not index_memory:
    print("NO")
else:
    for i, x in enumerate(il):
        if i not in index_memory.values() and counts[x] == 1:
            print(x, end=" ")

# https://www.eolymp.com/uk/submissions/9981532
