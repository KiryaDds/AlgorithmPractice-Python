# T17.6


def no_kwargs(average_num):
    def _no_kwargs(*args, **kw):
        if len(kw) != 0:
            msg = "Дозволені лише позиційні параметри!"
            raise PermissionError(msg)
        res = average_num(*args, **kw)
        return res
    return _no_kwargs


@no_kwargs
def f(*p, **kp):
    Eisum = 0
    imax = None

    for xi in p:
        Eisum += xi
        if imax is None:
            imax = xi
        if xi > imax:
            imax = xi

    if imax > Eisum:
        theta = True
        res = 1
    else:
        res = 0
        theta = False
        for xi in p:
            if xi > 0:
                res += xi
    return res, theta


if __name__ == "__main__":
    test_true = f(6, -12, 5)
    print(test_true)
    test1 = f(4, 13, f=2)
    print(test1)
