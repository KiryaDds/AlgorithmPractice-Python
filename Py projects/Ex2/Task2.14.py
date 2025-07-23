x = float(input('x= '))
y = float(input('y= '))
if (-2 <= y < 0) and (-1 <= x <= 1) or ((y >= 0) and ((x**2 + y**2) <= 4)):
    print('\033[32mТак, точка належить грибочку!')
else:
    print('\033[33mТочка знаходиться поза грибницею!')

non_stop = input()
