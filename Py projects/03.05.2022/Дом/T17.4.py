# T17.4


def is_all_string(f):
    def _is_all_string(*p):
        for el in p:
            if not isinstance(el, str):
                msg = "Wrong type " + str(type(el)) + " object: %s. 'Str' type expected." % el
                raise TypeError(msg)
        res = f(*p)
        return res
    return _is_all_string


@is_all_string
def f(*p):
    l = []
    for s in p:
        if s not in l:
            l.append(s)
    return l


if __name__ == "__main__":
    test_true = f("fff", "fff", "blabla", "bla")
    print(test_true)
    test1 = f(4, "5", "5", [12])
    print(test1)
