# T16_12

X = (1, -35.4, 67, -56.7, 10.3, -34, 40.0, 22.2, -12)
print("Вектор X:\n", X)
print()
# a)
GX1 = (X[e] for e in range(len(X)) if e % 2 == 0)
print("Елементи з генератор-виразу GX1 з парними індексами:")
for e in GX1:
    print(e, end='   ')
print()
# b)
GX2 = (X[e] for e in range(len(X)) if e % 2 != 0)
print("Елементи з генератор-виразу GX2 з непарними індексами:")
for e in GX2:
    print(e, end='   ')
print()
