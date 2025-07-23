# Завдання 13.6 by  Янголь Ярослав / Комп. мех / 2 курс


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



def polish_to_infix(expression):

    OPERATORS = {
                "+": 1,
                "-": 1,
                "*": 2,
                "/": 2,
                }
    st = Stack()
    res = ""

    return res




if __name__ == "__main__":

    print(polish_to_infix(input()))