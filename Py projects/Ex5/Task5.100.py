A = input("A = ")
V = input("Визначте, які символи будуть рахуватися:")
xmax = 0
xmin = len(A)
charmin = ""
charmax = ""
for i in V:
    x = A.count(i)
    if xmax < x:
        xmax = x
        charmax = i
    if xmin > x:
        xmin = x
        charmin = i
    print("\033[0mКількість символів \033[32m'{}' \033[0mдорівнює \033[35m{}".format(i, x))
print("\033[0mМінімальну кількість входжень у рядок (\033[33m{}\033[0m) має символ '\033[32m{}\033[0m'".format(xmin,
                                                                                                               charmin))
print("\033[0mМаксимальну кількість входжень у рядок (\033[33m{}\033[0m) має символ '\033[32m{}\033[0m'".format(xmax,
                                                                                                                charmax)
      )
input()
