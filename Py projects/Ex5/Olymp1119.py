piramyd_char, h = input().split()
char_amount = 1
space_amount = int(h) - 1
max_char_amount = (int(h) / 2) * (2 * char_amount + (int(h) - 1) * 2) + (int(h) / 2) * (2 * space_amount + (int(h) - 1)
                                                                                        * (-1))
print(int(max_char_amount))
for i in range(int(h)):
    chars = str(piramyd_char) * char_amount
    spaces = " " * space_amount
    piramid = str(spaces + chars)
    print(piramid)
    char_amount += 2
    space_amount -= 1

# https://www.e-olymp.com/uk/submissions/9541364
