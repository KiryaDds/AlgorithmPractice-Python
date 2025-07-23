square = str(input('Оберіть область, належність точки до якої ви бажаєте перевірити. '
                   'Доступні варіанти: а, б, в, г, д, е: '))
x = float(input('x= '))
y = float(input('y= '))

if square == 'а':  # Перевірка обраної області для здійснення відповідних розрахунків
    if (0 <= x <= 2) and (0 <= y <= 1):
        print('Ця точка належить заданій області: ', square)
    else:
        print('Ця точка НЕ належить заданій області: ', square)
elif square == 'б':
    if (x >= 0) and ((abs(x) + abs(y)) <= 2) or ((x < 0) and ((x**2 + y**2) <= 4)):
        print('Ця точка належить заданій області: ', square)
    else:
        print('Ця точка НЕ належить заданій області: ', square)
elif square == 'в':
    if (abs(x) + abs(y) >= 2) and ((x**2 + y**2) <= 4):
        print('Ця точка належить заданій області: ', square)
    else:
        print('Ця точка НЕ належить заданій області: ', square)
elif square == 'г':
    if x**2 + y**2 >= 4:
        if abs(x) <= 2 and abs(y) <= 2 and not(x > 0 and y > 0):
            print('Ця точка належить заданій області: ', square)
        else:
            print('Ця точка НЕ належить заданій області: ', square)
    else:
        print('Ця точка НЕ належить заданій області: ', square)
elif square == 'д':
    if (y >= x) and (y + x >= 0) and (y <= 1):
        print('Ця точка належить заданій області: ', square)
    else:
        print('Ця точка НЕ належить заданій області: ', square)
elif square == 'е':
    if (x >= -1) and (x <= 1) and (y >= -1) and (y <= 1):
        print('Ця точка належить заданій області: ', square)
    else:
        print('Ця точка НЕ належить заданій області: ', square)
else:
    print('Ви не обрали область...')

non_exit = input()
