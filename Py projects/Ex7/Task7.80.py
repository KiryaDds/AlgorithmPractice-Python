from collections import namedtuple

Human = namedtuple("X", ["Sex", "Height"])

n = int(input("n = "))
A = []
for i in range(n):
    S = input("Стать: 'M' or 'F' ")
    H = input("Зріст: ")
    A.append(Human(S, H))

print(A)


avr_h = 0
females = 0
for x in A:
    if x.Sex == "F":
        avr_h += int(x.Height)
        females += 1
avr_h = avr_h / females

print("Середній зріст у жінок: ", avr_h)


maxHeight = 0
for x in A:
    if x.Sex == "M":
        if maxHeight < int(x.Height):
            maxHeight = int(x.Height)

print("Максимальний зріст у чоловіків {}".format(maxHeight))


same_h = False
same_h_value = 0
for x in A:
    for i in A[A.index(x):len(A)]:
        if int(x.Height) == int(i.Height):
            same_h_value = int(x.Height)
            same_h = True
            break

if same_h is True:
    print("У групі є дві людини однакового зросту, а саме {}".format(same_h_value))
else:
    print("Людей однакового зросту немає")
