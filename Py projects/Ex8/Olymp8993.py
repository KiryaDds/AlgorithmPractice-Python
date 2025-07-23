a = input()
b = input()
da, db = {}, {}

for x in a:
    if x in da:
        da[x] += 1
    else:
        da[x] = 1

for x in b:
    if x in db:
        db[x] += 1
    else:
        db[x] = 1

ok = True
for k, v in db.items():
    if k not in da:
        ok = False
        break
    if db[k] > da[k]:
        ok = False
        break

if ok:
    print("Ok")
else:
    print("No")

# https://www.eolymp.com/uk/submissions/9981567
