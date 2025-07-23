# auto - brend, id, owner
# key - id, value (brend, owner)

cars = {}
n = int(input("n = "))
for _ in range(n):
    id = int(input("ID: "))
    brend = input("Brend: ")
    name = input("Owner: ")
    cars[id] = (brend, name)

by_brend = {}
for id, info in cars.items():
    brand = info[0]
    if brand in by_brend:
        by_brend[brand].append(info[1])
    else:
        by_brend[brand] = [info[1]]

print(by_brend)

for brand, names in by_brend.items():
    print("\nNumber of {} is {}".format(brand, len(names)))
    for name in names:
        print("Owner " + name, end=" ")
