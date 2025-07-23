Chosen_task = " "
while Chosen_task != "":
    Chosen_task = input("\nВиберіть завдання, яке потрібно виконати (можливі варіанти: а, б, в, г, д): ")
    print("Щоб закінчити виконання програми, натицніть 'Enter' без введення під час повторення запиту.")
    text = input("text = ")  # str(input("..."))

    if Chosen_task == "а":
        n = len(text)
        # DIGS = "0123456789"
        for i in range(n):          # Або варіант, де замість text[i] є х, який є більш пітонівський.
            if text[i].isdigit():       # if text[i] == "0" or ...
                continue
            # if text[i] in DIGS:
            #     continue
            print(text[i], end="")
            if text[i] == "+" or text[i] == "-":
                print(text[i], end="")

    elif Chosen_task == "б":
        n = len(text)
        for i in range(n - 1):
            if text[i] == "+" and text[i + 1].isdigit():
                continue
            print(text[i], end="")

    elif Chosen_task == "в":
        n = len(text)
        print(text[0], end="")
        for i in range(1, n):
            if text[i] == "b" and text[i - 1] == "c":
                continue
            print(text[i], end="")      # print(text.replace("cb", "c"), end="")

    elif Chosen_task == "г":
        print(text.replace("ph", "f"), end="")

    elif Chosen_task == "д":
        n = len(text)
        text1 = ""
        prev = text[0]
        for x in text:  # from t[0] to t[len(t) - 1]
            if x == " " and prev == " ":
                continue
            prev = x
            text1 += x
            print("x = {}, text = {}".format(x, text1))

    else:
        print("Виконання програми закінчено. (Можливо, Ви не правильно обрали завдання)")
        break
input()
