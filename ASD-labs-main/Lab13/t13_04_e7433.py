# Завдання 13.4 by  Янголь Ярослав / Комп. мех / 2 курс


class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            exit(1)
        else:
            return self.items.pop()
    
    def back(self):
        if len(self.items) == 0:
            exit(1)
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()


def convert(num, base):

    conv_cont = Stack()

    while num > 0:
        conv_cont.push(num % base)
        num //= base
        converted = ""

    while not conv_cont.empty():
        digit = conv_cont.pop()
        if digit <= 9:
            converted += str(digit)
        else:
            converted += "[" + str(digit) + "]"

    return converted


if __name__ == "__main__":

    A = int(input())
    P = int(input())
    res = convert(A, P)
    print(res)


