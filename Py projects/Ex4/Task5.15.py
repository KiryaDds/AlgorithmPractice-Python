import math
n = int(input("n = "))
for q in range(2, int(math.sqrt(n) + 1)):
    if n % q**2 == 0 and n % (q**3) != 0:
        print(q)

non_stop = input()
