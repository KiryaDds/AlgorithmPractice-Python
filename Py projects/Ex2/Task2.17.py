a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

if a < b and a < c:
    min_value = a

elif b < a and b < c:
    min_value = b

elif c < a and c < b:
    min_value = c

elif a == b and a < c:
    min_value = '{0} (a) = {1} (b)'

elif a == c and a < b:
    min_value = '{0} (a) = {2} (c)'

elif b == c and c < a:
    min_value = '{1} (b) = {2} (c)'

else:
    min_value = 'жодне з введених'

print('Найменшим(и) з введених чисел є', min_value .format(a, b, c))

non_stop = input()
