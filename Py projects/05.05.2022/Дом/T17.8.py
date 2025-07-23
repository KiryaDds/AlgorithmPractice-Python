# T17.8


def mydec(f):
    def _mydec(*args, **kw):
        if len(args) != 0:
            msg = "Дозволені лише ключові параметри!"
            raise PermissionError(msg)
        for k, v in kw.items():
            if not (isinstance(k, str) and isinstance(v, int)):
                msg = "Wrong type " + str(type(v)) + " object: %s. 'Int' type expected." % v
                raise TypeError(msg)
        res = f(*args, **kw)
        return res
    return _mydec


@mydec
def f(*args, **kw):
    c = 0; word = None
    for k, v in kw.items():
        if word is None:
            word = k
        if v > c:
            c = v; word = k
    return word


if __name__ == "__main__":
    test_true = f(cat=4, rat=3, dog=10)
    print("Найбільшу кількість разів зустрічається слово:", test_true)
    test1 = f(someone="Дядько Толя ", did="випив ", amount=9, of_what=" літрів пива")
    print(test1)
    test2 = f(56, 4, 4.3, 5, num=9, what=" літрів пива")
    print(test2)
