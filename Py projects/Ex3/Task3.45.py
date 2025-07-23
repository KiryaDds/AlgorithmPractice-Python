n = int(input("n = "))
if n < 0:
    print("\033[32mВедено недодатнє число!")
else:
    i = 1 if n % 2 != 0 else 2
    x = i
    while i < n:
        i += 2
        x *= i
    print("y = ", x)
non_stop = input()
