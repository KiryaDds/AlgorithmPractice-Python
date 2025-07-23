"""Описати клас-домішок CompareMixin (див. задачу Т18.10).

Вагою числового списку назвемо суму модулів його елементів.
Описати клас зважений список WeightedList, що є нащадком стандартного
класу list та реалізує відношення < у відповідності з вагою списків.
Описати клас нащадок цього класу та домішку CompareMixin
FullOrderWeightedList – зважений список з повним порядком.
Ввести список зважених списків з повним порядком та перевірити, чи є всі
вони у сенсі заданого порядку (мають рівну вагу).
"""


class CompareMixin:
    def __eq__(self, value):
        return not self < value and not value < self

    def __ne__(self, value):
        return self < value or value < self

    def __gt__(self, value):
        return value < self

    def __le__(self, value):
        return not value < self

    def __ge__(self, value):
        return not self < value


class WeightedList(list):
    def __init__(self):
        list.__init__(self)

    @property
    def weight(self):
        for x in range(len(self)):
            if x < 0: self[x] = abs(x)
        return sum(self)

    def __lt__(self, value):
        return self.weight < value.weight


class FullOrderWeightedList(CompareMixin, WeightedList):
    pass


if __name__ == "__main__":
    h1 = FullOrderWeightedList(); h2 = FullOrderWeightedList(); h3 = FullOrderWeightedList(); h4 = FullOrderWeightedList()
    h1.extend([5, 7, 9, -0]); h2.extend([27, 1, 13, -20]); h3.extend([10, 6, 4]); h4.extend([11, 6, 4])
    check_ls = [h1, h2, h3, h4]     # Усі списки крім h3 мають вагу 21
    print(check_ls); print()
    for i in range(len(check_ls)):
        for j in range(i+1, len(check_ls)):
            if check_ls[i].weight == check_ls[j].weight:
                print("У сенсі заданого порядку є %s та %s" % (check_ls[i], check_ls[j]))
