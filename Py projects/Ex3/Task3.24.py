n = float(input("Введіть перше число послідовності: "))
sign_counter = 0

print("Щоб побачити результат, введіть \033[33m\033[1m'0'.")
# \033[33m\033[1m -- ANSII код, що фарбує текст у жовтий та робить жирний шрифт

while n != 0:

    if n > 0:
        n = float(input("\033[0m\033[0mВведіть наступне число послідовності: "))
        if n < 0:
            sign_counter += 1
# \033[0m\033[0m -- скидує значення кольору та ефектів шрифта

    if n < 0:
        n = float(input("Введіть наступне число послідовності: "))
        if n > 0:
            sign_counter += 1

if sign_counter == 1:
    amount_text = "раз"
elif sign_counter == 2:
    amount_text = "рази"
elif sign_counter == 3:
    amount_text = "рази"
elif sign_counter == 4:
    amount_text = "рази"
else:
    amount_text = "разів"
# "Відмінює" текст

print("\033[34mЗміна знаку чисел у введеній послідовності відбулася {} {}.".format(sign_counter, amount_text))
# \033[34m -- фарбує текст у блакитний колір
# https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html#tsveta -- звідси взяв ці коди

non_stop = input()
