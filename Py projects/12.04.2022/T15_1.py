# Програма потребуватиме введення доки користувач не напише слово "досить".
# Кількість виключень типу рахує завдяки методу .add() класу M_set (якщо не забороняється).


from M_set import *

errset = M_set()

while True:
    inps = input()
    try:
        if inps == "досить":
            break
        if int(inps) > 9:
            errset.add(RuntimeError)
            raise RuntimeError
        if int(inps) < 0:
            errset.add(TypeError)
            raise TypeError
        if 0 <= int(inps) <= 9:
            errset.add(ValueError)
            raise ValueError

    except (RuntimeError, TypeError, ValueError):
        pass

print("Кількість помилок кожного з типів: ", errset)
