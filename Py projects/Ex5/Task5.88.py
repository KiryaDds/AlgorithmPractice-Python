text = input("text = ")
count = 0
for x in text:
    if x in "+-*":
        count += 1
print(count)

input()
