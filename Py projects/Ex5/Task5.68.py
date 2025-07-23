d = "0"
sumd = int(d)
while True:
    d = str(input("Введіть число с його знаком попереду: "))
    if d != ".":
        sumd += int(d)
    else:
        break
print(sumd)
input()
