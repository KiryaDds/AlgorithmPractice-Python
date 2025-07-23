x = float(input('x= '))
y = float(input('y= '))

if (x >= 0) and (y >= 0):
    quarter = '1-му'
    print('Точка з координатами ({}; {}) належить '.format(x, y), quarter, ' координатному квадранту.')
elif (x <= 0) and (y >= 0):
    quarter = '2-му'
    print('Точка з координатами ({}; {}) належить '.format(x, y), quarter, ' координатному квадранту.')
elif (x <= 0) and (y <= 0):
    quarter = '3-му'
    print('Точка з координатами ({}; {}) належить '.format(x, y), quarter, ' координатному квадранту.')
elif (x >= 0) and (y <= 0):
    quarter = '4-му'
    print('Точка з координатами ({}; {}) належить '.format(x, y), quarter, ' координатному квадранту.')
else:
    print('Як так отрималось, що ви потрапили за межі декартової системи координат?')

non_stop = input()