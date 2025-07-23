# Завдання для самостійної роботи за 05.05.2022


def is_num(average_num):
    def _is_num(*some):
        for el in some:
            if not (isinstance(el, float) or isinstance(el, int)):
                msg = "Wrong type " + str(type(el)) + " object: %s" % el
                raise TypeError(msg)
        res = average_num(*some)
        return res
    return _is_num


@is_num
def average_num(*nums):
    a = 0
    for num in nums:
        a += num
    return a / len(nums)


if __name__ == "__main__":
    av = average_num(1, 3, 4.7)
    print(av)
    av1 = average_num(56, "1")
    print(av1)
