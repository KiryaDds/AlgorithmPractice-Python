from cmath import *
x = complex(input("x = "))

r = sqrt(x.real**2 + x.imag**2)
r1 = abs(x)
print(r, r1)

print(tan(x.real/x.imag))

a = complex(input())
b = complex(input())
c = complex(input())

if abs(a) > 0:
    D = sqrt(b**2 - 4 * a * c)
    x1 = (-b - D) / 2 / a
    x2 = (-b - D) / 2 / a
    print(x1, x2)

non_stop = input()
