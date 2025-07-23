# Завдання 12.3 by  Янголь Ярослав / Комп. мех / 2 курс


class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        print("ok")

    def pop(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items.pop())
    
    def back(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items[len(self.items) - 1])
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        print("ok")

    def exit(self):
        print("bye")
        exit(0)


if __name__ == "__main__":
    ts = Stack()
    while True:
        line = input().split()
        if line[0] == "push":
            ts.push(line[1])
        if line[0] == "pop":
            ts.pop()
        if line[0] == "back":
            ts.back()
        if line[0] == "size":
            print(ts.size())
        if line[0] == "clear":
            ts.clear()
        if line[0] == "exit":
            ts.exit()