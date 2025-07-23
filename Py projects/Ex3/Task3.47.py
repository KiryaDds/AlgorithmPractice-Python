n = int(input("n = "))
if n < 0:
    print("\033[32mFalse")
else:
    p = 1
    for i in range(1, n + 1):       # i = 1, 2, ... , n
        p = (1 / i**2 + 1) * p
    print("p = {}".format(p))
Non_stop = input()
