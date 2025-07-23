# Завдання 12.4 by  Янголь Ярослав / Комп. мех / 2 курс


class Stack:

    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, item):
        self.items.append(item)
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)

    def pop(self):
        if self.items:
            item = self.items.pop()
            if item == self.min_items[-1]:
                self.min_items.pop()
            return item

    def min_item(self):
        if self.min_items:
            print(self.min_items[-1])


if __name__ == "__main__":
    ts = Stack()
    n = int(input())
    for i in range(n):
        line = input().split()
        if int(line[0]) == 1:
            ts.push(int(line[1]))
        if int(line[0]) == 2:
            ts.pop()
        if int(line[0]) == 3:
            ts.min_item()
