n = int(input("n = "))
if n < 3:
    print("\033[33mЗамало чисел для обчислення.")
else:
    neighbor_number = 0
    neighbor_existence = False
    for i in range(1, n - 1):
        if neighbor_existence is True:
            neighbor_previous = middle
            middle = neighbor_next
            neighbor_next = input("Введіть наступне число: ")
            if neighbor_previous < middle and neighbor_next < middle:
                neighbor_number += 1
        elif neighbor_existence is False:
            neighbor_previous = input("Введіть перше число: ")
            middle = input("ВВедіть друге число: ")
            neighbor_next = input("Введіть третє число: ")
            neighbor_existence = True
            if neighbor_previous < middle and neighbor_next < middle:
                neighbor_number += 1
    print("\033[32mКількість чисел більших за своїх сусідів: ", neighbor_number)
non_stop = input()
