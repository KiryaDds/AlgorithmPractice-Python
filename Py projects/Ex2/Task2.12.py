a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0):
    print('Трикутник існує')
else:
    print('Трикутник не існує')
