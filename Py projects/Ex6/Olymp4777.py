from math import *

x1A, y1A, x1B, y1B = map(int, input().split())
x2A, y2A, x2B, y2B = map(int, input().split())

length_1 = sqrt((x1B - x1A)**2 + (y1B - y1A)**2)
length_2 = sqrt((x2B - x2A)**2 + (y2B - y2A)**2)

sum_vect_x = (x1B - x1A) + (x2B - x2A)
sum_vect_y = (y1B - y1A) + (y2B - y2A)

scalar_mult = (x1B - x1A)*(x2B - x2A) + (y1B - y1A)*(y2B - y2A)
vect_mult = (x1B - x1A)*(y2B - y2A) - (x2B - x2A)*(y1B - y1A)

square = str(abs(vect_mult/2))


def digits(s):
    for j in range(len(s)):
        if not(s[j] == ".") and j == len(s):
            s += "." + "0" * 9
        elif s[j - 1] == ".":
            while 9 > len(s[j:len(s)]):
                s += "0"
    return s


print(round(length_1, 9), round(length_2, 9))
print(str(round(sum_vect_x, 9)) + ".000000000", str(round(sum_vect_y, 9)) + ".000000000")
print(str(scalar_mult) + ".000000000", str(vect_mult) + ".000000000")
print(digits(square))

# https://www.eolymp.com/uk/submissions/9971275
