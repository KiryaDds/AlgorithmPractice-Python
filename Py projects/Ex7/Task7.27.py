from collections import namedtuple


field = namedtuple("field", ['H', 'I'])
letters = ("A", "B", "C", "D", "E", "F", "G", "H")
nnum = (1, 2, 3, 4, 5, 6, 7, 8)


def input_field(comment):
    print(comment)
    while True:
        H = input("Letter: ")
        if H in letters:
            break

    while True:
        I = int(input("Digit: "))
        if 1 <= I <= 8:
            break
        return field(H, I)


def queen_check(h1, h2):
    return h1.H == h2.H or h1.I == h2.I or h1.I - h2.I == letters.index(h1.H) - letters.index(h2.H)


x = input_field("First")
y = input_field("Second")

if queen_check(x, y):
    print("Check")
else:
    print("Don't check")
