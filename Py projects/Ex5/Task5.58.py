text = input("text = ")
n = len(text)
comma1_index = 0
k = 0
j = 0

for i in range(1, n + 1, 1):
    if text[i] == ",":
        k = i
        break

for i in range(n - 1, 0, -1):
    if text[i] == ",":
        j = i
        break

print("Перша кома має номер: ", k)
print("Остання кома має номер: ", j)

input()
