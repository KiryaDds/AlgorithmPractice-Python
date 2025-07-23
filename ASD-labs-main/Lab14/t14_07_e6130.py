# Завдання 14.7 by  Янголь Ярослав / Комп. мех / 2 курс


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deck:

    def __init__(self):
        self.front = None
        self.back = None

    def __del__(self):
        while self.front is not None:
            node = self.front
            self.front = self.front.next
            del node
        self.back = None

    def empty(self):
        return self.front is None and self.back is None
    
    def push_front(self, item):
        node = Node(item)
        node.next = self.front
        if not self.empty():
            self.front.prev = node
        else:
            self.back = node
        self.front = node
        print("ok")

    def push_back(self, item):
        elem = Node(item)
        elem.prev = self.back
        if not self.empty():
            self.back.next = elem
        else:
            self.front = elem
        self.back = elem
        print("ok")

    def pop_front(self):
        if self.empty():
            print("error")
        else:
            node = self.front
            item = node.item
            self.front = node.next
            if self.front is None:
                self.back = None
            else:
                self.front.prev = None
            del node
            print(item)
    
    def pop_back(self):
        if self.empty():
            print("error")
        else:
            node = self.back
            item = node.item
            self.back = node.prev
            if self.back is None:
                self.front = None
            else:
                self.back.next = None
            del node
            print(item)
    
    def get_front(self):
        if self.empty():
            print("error")
        else:
            item = self.front.item
            print(item)

    def get_back(self):
        if self.empty():
            print("error")
        else:
            item = self.back.item
            print(item)
    
    def size(self):
        if self.empty():
            return 0
        count = 0
        node = self.front
        while node is not None:
            count += 1
            node = node.next
        return count
    
    def clear(self):
        while not self.empty():
            #self.pop_front()
            node = self.front
            item = node.item
            self.front = node.next
            if self.front is None:
                self.back = None
            else:
                self.front.prev = None
            del node
        print("ok")

    def exit(self):
        print("bye")
        exit(0)

if __name__ == "__main__":
    dc = Deck()
    while True:
        line = input().split()
        if line[0] == "push_front":
            dc.push_front(line[1])
        elif line[0] == "pop_front":
            dc.pop_front()
        elif line[0] == "push_back":
            dc.push_back(line[1])
        elif line[0] == "pop_back":
            dc.pop_back()
        elif line[0] == "front":
            dc.get_front()
        elif line[0] == "back":
            dc.get_back()
        elif line[0] == "size":
            print(dc.size())
        elif line[0] == "clear":
            dc.clear()
        elif line[0] == "exit":
            dc.exit()
