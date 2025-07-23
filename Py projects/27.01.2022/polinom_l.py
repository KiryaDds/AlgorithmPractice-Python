# Модуль реалізації поліномів. Модель - список.
"""Даний модуль реалізує дії над поліномами.

   Поліном представлений у вигляді списка.
     Зберігаємо всі коефіцієнти по спаданню степеней.
     P[0]<>0, виключення - це нуль-поліном: P=[0].

    Функції:
    get() -> P - Введення поліному з клавіатури.
    str_to_poly(s) -> P - Перетворення рядка у поліном.
    Рядок повинен мати вигляд, наприклад: 3*x^3 + 2*x^1 + -1.5*x^0
    put(name, P) - Показати поліном P у вигляді рядка
    value(P, t) -> y - Значення поліному P у точці t.
    maxp(P) -> y - max по модулю коефіцієнт P;
    minp(P) -> y - min по модулю коефіцієнт P;
    add(P, Q) -> R - Сума поліномів P + Q.
    sub(P, Q) -> R - Різниця поліномів P + Q.
    mul(P, Q) -> R - Добуток поліномів P * Q.
    divmod(P, Q) -> (H, R) - частка і остача P / Q, де P = H*Q+R.
    deriv(P [, n = 1]) -> R - n-та похідна поліному P.
    integ(P, a, b) -> y - Визначений інтеграл від поліному P.
    integn(P) -> R - Iнтеграл від поліному P.
    eg(P, Q) -> b - Чи є P рівний Q ?
    ne(P, Q) -> b - Чи є P не рівний Q ?
"""


def _delzeroes(P):
    """
    Видаляє з P нульові коефіцієнти.
    Якщо всі коефіцієнти нулі, то повертає нуль-поліном 0*x**0.
    """

    if P == [0]:
        pass
    else:
        while len(P) > 1 and P[0] == 0:
            P.pop(0)

    return P


def get() :
    '''Введення поліному.

    '''
    while True :
        s = input("Введіть поліном в вигляді послідовності КОЕФ СТЕП:\n")
        s = s.split(); n = len(s)
        if n % 2 == 0 :
            C = []; K = []; i = 0; f = True
            while i < n :
                c = float(s[i]); i +=1; k = int(s[i])
                if k < 0 : # перевірка степенів (має бути k>=0)
                    f = False
                    print("Помилка: СТЕП має бути >= 0")
                    break
                C.append(c); K.append(k); i +=1
            if f : break
        else : print("Помилка: кількість(КОЕФ)<>кількість(СТЕП)")
    if len(C) == 0 :
        P = [0]
    else :
        n = max(K); P = [0]*(n+1)
        for k in range(len(K)) :
            P[n-K[k]] = C[k]
        P = _delzeroes(P)
        print(P)
    return P


def str_to_pol(s):
    """Перетворення рядка у поліном.

       Рядок повинен мати вигляд, наприклад: 3*x^3 + 2*x^1 + -1.5*x^0.
       Пробіли між коефіцієнтами та степенями не допускаються.
       Від'ємні коефіцієнти записувати як у прикладі вище.
    """

    P = []
    s = s.split(" + ")
    for i in range(len(s)):
        n = s[i].split("*x^")
        P.append(int(n[0]))

    return P


def put(name, P, a=0):
    """Показати поліном P у вигляді рядка.

       Рядок буде мати вигляд (наприклад):
       2.5*x^3 + 0.5*x - 1.5
    """

    s = ""
    xs = "*x"
    if a != 0:
        if a > 0:
            xs = "*(x-" + str(a) + ")"
        elif a < 0:
            xs = "*(x+" + str(a) + ")"

    for i in range(len(P)):
        if P[i] > 0:
            if i == len(P) - 1:
                s += " + " + str(float(P[i]))
            elif i == len(P) - 2:
                s += " + " + str(float(P[i])) + xs
            else:
                s += " + " + str(float(P[i])) + xs + "^" + str(len(P) - i - 1)
        elif P[i] < 0:
            if i == len(P) - 1:
                s += " - " + str(float(P[i])).lstrip("-")
            elif i == len(P) - 2:
                s += " - " + str(float(P[i])).lstrip("-") + xs
            else:
                s += " - " + str(float(P[i])).lstrip("-") + xs + "^" + str(len(P) - i - 1)
    s = s.lstrip(" + ")

    print(name + s)


def value(P, t):
    """Значення поліному P у точці t.

    """

    s = 0
    for i in range(len(P)):
        s += P[len(P) - i - 1] * t**i

    return s


def maxp(P):
    """max по модулю коефіцієнт P.

    """

    y = P[0]
    for i in range(len(P)):
        y = max(y, P[i])
    return y


def minp(P):
    """min по модулю коефіцієнт P.

    """

    y = P[0]
    for i in range(len(P)):
        y = min(y, P[i])

    return y


def add(P, Q):
    """
    Сума поліномів P + Q.
    """

    R = []
    n = abs(len(P) - len(Q))
    if len(P) >= len(Q):
        minPoli = Q
        maxPoli = P
    else:
        minPoli = P
        maxPoli = Q

    minP = []
    for i in range(n):
        minP.append(0)

    minPoli += minP

    for i in range(len(P)):
        R.append(maxPoli[i] + minPoli[i])

    return _delzeroes(R)


def sub(P, Q):
    """
    Різниця поліномів P - Q.
    """

    R = []
    n = abs(len(P) - len(Q))
    if len(P) >= len(Q):
        minPoli = Q
        maxPoli = P
    else:
        minPoli = P
        maxPoli = Q

    minP = []
    for i in range(n):
        minP.append(0)

    minPoli += minP

    for i in range(len(P)):
        R.append(maxPoli[i] - minPoli[i])

    return _delzeroes(R)


def mul(P, Q):
    """
    Добуток поліномів P * Q.
    """

    if P == [0] or Q == [0] or P == 0 or Q == 0:
        return [0]

    else:
        n0_P = len(P) - 1
        n0_Q = len(Q) - 1
        n0_R = n0_P + n0_Q

        R = list()
        for k in range(n0_R + 1):
            R.append(0)

        for i in range(n0_P + 1):
            for j in range(n0_Q + 1):
                R[i + j] += (P[i] * Q[j])

    return R


def divmod(P, Q):
    """Частка (H) і остача (R) ділення полінома P на Q, де P = H*Q+R.

    """
    R = P.copy()
    H = [0]  # P=H*Q+R
    kQ = len(Q) - 1
    cQ = Q[0]
    if kQ == 0 and cQ == 0:
        err = 1  # Ділення на нуль-поліном
    else:
        err = 0
        kR = len(R) - 1
        i = kR - kQ
        while i >= 0:
            o = [0] * (i + 1)
            o[0] = R[0] / cQ
            R = sub(R, mul(Q, o))
            H = add(H, o)
            kR = len(R) - 1
            i = kR - kQ
    return err, H, R


def deriv(P, n=1):
    """n-та похідна поліному P, за угодою 1-а.

    """
    R = []
    for i in range(len(P) - 1):
        R.append(P[i] * (len(P) - i - 1))

    return _delzeroes(R)


def integ(P, a, b):
    """Визначений інтеграл на відрізку [a,b] від поліному P.

    """

    s = 0
    for i in range(len(P)):
        n = len(P) - i - 1
        k = P[i] / (n + 1)
        s += k * b**(n + 1) - k * a**(n + 1)

    return s


def eq(P, Q):
    """Чи є P рівний Q ?

    """

    if P == Q:
        b = True
    else:
        b = False
    return b


def ne(P, Q):
    """Чи є P не рівний Q ?

    """

    if P != Q:
        b = True
    else:
        b = False
    return b


def tailor(P, a):       # Завдання 3;
    f = 1
    y = P
    R = []
    for n in range(len(P)):
        if n > 0:
            f *= n
            y = deriv(y)
        R.append(value(y, 2) // f)

    P = R
    s = ""
    xs = "*x"
    if a != None:
        if a > 0:
            xs = "*(x-" + str(a) + ")"
        elif a < 0:
            xs = "*(x+" + str(a) + ")"

    for i in range(len(P)):
        if P[i] > 0:
            if i == 0:
                s += " + " + str(float(P[i]))
            elif i == 1:
                s += " + " + str(float(P[i])) + xs
            else:
                s += " + " + str(float(P[i])) + xs + "^" + str(i)
        elif P[i] < 0:
            if i == 0:
                s += " - " + str(float(P[i])).lstrip("-")
            elif i == 1:
                s += " - " + str(float(P[i])).lstrip("-") + xs
            else:
                s += " - " + str(float(P[i])).lstrip("-") + xs + "^" + str(i)
    s = s.lstrip(" + ")

    return s


if __name__ == '__main__':
    # Тестування функцій :
    print("\033[031mТестування!\033[039m")
    P = get()                                       # 1 2 2 1 1 0
    put("P(x):=", P)
    print("")
    print("Мінімальний коефіцієнт: ", minp(P))
    print("Максимальний коефіцієнт: ", maxp(P))
    print("")
    put("Похідна P'(x):=", deriv(P))
    print("Інтеграл P:=", str(integ(P, 2, 5)))
    print("")
    print("Значення P у точці 5: ", value(P, 5))
    print("")
    print("1*x^2 + -2*x^1 + 1*x^0 у вигляді поліному(списку): ", str_to_pol("1*x^2 + -2*x^1 + 1*x^0"))
    print("")
    R = get()                                       # 1 2 -2 1 1 0
    put("R(x):=", R)
    Q = get()                                       # 1 1 -1 0
    put("Q(x):=", Q)
    print("")
    print("Чи є P не рівний R: ", ne(P, R))
    print("Чи є P рівний Q: ", eq(P, Q))
    print("")
    print("Сума P i Q: ", add(P, Q))
    print("Різниця P i Q: ", sub(P, Q))
    print("")
    print("Добуток P i Q: ", mul(P, Q))
    print("")
    print("")
    print("")

    A = [1]
    for i in range(10):
        A = mul(A, [1, 2])

    put("P(x):= ", [1, 2])
    put("R(x):= (x+2)^10 := ", A)
    print()
    print("Fормула Тейлора (x^6+2x-1, x-2):")
    put("P(x):= ", [6, 0, 0, 0, 0, 2, -1])
    print("P(x)= ", tailor([1, 0, 0, 0, 0, 2, -1], 2))

    '''err, H, Z = divmod(R, Q)
    if not err:
        put("Частка H(x):=", H)
        put("Остача Z(x):=", Z)
        print("Перевірка R(x)=H(x)*Q(x)+Z(x):=", eq(R, add(mul(H, Q), Z)))'''