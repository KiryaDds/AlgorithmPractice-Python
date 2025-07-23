# T17.7


def no_args(average_num):
    def _no_args(*args, **kw):
        if len(args) != 0:
            msg = "Дозволені лише ключові параметри!"
            raise PermissionError(msg)
        res = average_num(*args, **kw)
        return res
    return _no_args


@no_args
def f(*args, **kw):
    s = str([x for x in kw])
    return s


if __name__ == "__main__":
    na = f(someone="Дядько Толя ", did="випив ", amount=9, of_what=" літрів пива")
    print(na)
    na1 = f(56, 4, 4.3, 5, num=9, what=" літрів пива")
    print(na1)
