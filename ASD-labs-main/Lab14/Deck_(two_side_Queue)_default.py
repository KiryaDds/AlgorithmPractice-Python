class Deck:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push_front(self, item):
        self.items.append(item)
        print("ok")

    def push_back(self, item):
        self.items.insert(0, item)
        print("ok")

    def pop_front(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items.pop(0))
    
    def pop_back(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items.pop())
    
    def front(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items[0])

    def back(self):
        if len(self.items) == 0:
            print("error")
        else:
            print(self.items[-1])
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        print("ok")

    def exit(self):
        print("bye")
        exit(0)


if __name__ == "__main__":

    qe = Deck()
    while True:
        line = input().split()
        if line[0] == "push_front":
            qe.push_front(line[1])
        if line[0] == "pop_front":
            qe.pop_front()
        if line[0] == "push_back":
            qe.push_back(line[1])
        if line[0] == "pop_back":
            qe.pop_back()
        if line[0] == "front":
            qe.front()
        if line[0] == "back":
            qe.back()
        if line[0] == "size":
            print(qe.size())
        if line[0] == "clear":
            qe.clear()
        if line[0] == "exit":
            qe.exit()
