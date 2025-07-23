# Завдання 14.6 by  Янголь Ярослав / Комп. мех / 2 курс


class Queue:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        print("ok")

    def pop(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items.pop(0))
    
    def front(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items[0])
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        print("ok")

    def exit(self):
        print("bye")
        exit(0)


if __name__ == "__main__":

    qe = Queue()
    while True:
        line = input().split()
        if line[0] == "push":
            qe.push(line[1])
        if line[0] == "pop":
            qe.pop()
        if line[0] == "front":
            qe.front()
        if line[0] == "size":
            print(qe.size())
        if line[0] == "clear":
            qe.clear()
        if line[0] == "exit":
            qe.exit()


