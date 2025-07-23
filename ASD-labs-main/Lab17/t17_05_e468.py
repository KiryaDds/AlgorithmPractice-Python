# Завдання 17.5 by  Янголь Ярослав / Комп. мех / 2 курс


class Queue:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)
    
    def front(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()


class Node:
    
    def __init__(self, key):
        self.mLeftChild = self.mRightChild = None
        self.mKey = key

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def __str__(self):
        return str(self.mKey)


class BinaryTree(Node):

    def __init__(self, key):
        super().__init__(key)
        self.mParent = None

    def hasLeft(self) -> bool:
        return self.mLeftChild is not None

    def hasRight(self) -> bool:
        return self.mRightChild is not None
    
    def hasNoChildren(self) -> bool:
        return self.mLeftChild is None and self.mRightChild is None

    def setNode(self, item):
        if isinstance(item, BinaryTree):
            self.mKey = item.mKey
            self.mLeftChild = item.mLeftChild
            self.mRightChild = item.mRightChild

            if self.mLeftChild != None:
                self.mLeftChild.mParent = self
            if self.mRightChild != None:
                self.mRightChild.mParent = self
        else:
            self.mKey = item
    
    def setLeft(self, item):
        if isinstance(item, BinaryTree):
            self.mLeftChild = item
        elif self.hasLeft():
            self.mLeftChild.setNode(item)
        else:
            self.mLeftChild = BinaryTree(item)
        self.mLeftChild.mParent = self

    def setRight(self, item):
        if isinstance(item, BinaryTree):
            self.mRightChild = item
        elif self.hasRight():
            self.mRightChild.setNode(item)
        else:
            self.mRightChild = BinaryTree(item)
        self.mRightChild.mParent = self

    def removeLeft(self):
        self.mLeftChild = None

    def removeRight(self):
        self.mRightChild = None

    def isLeftChild(self):
        return self.mParent and self.mParent.mLeftChild == self

    def isRightChild(self):
        return self.mParent and self.mParent.mRightChild == self

    def removeSelfFromParent(self):
        if self.mParent is not None:
            if self.isLeftChild():
                self.mParent.mLeftChild = None
            else:
                self.mParent.mRightChild = None

    def __str__(self):
        return str(self.mKey)
    
    
def DFS(root):
    
    if child_queue.empty():
        return True
    
    fc = child_queue.pop()
    if root.key() < fc.key():
        root.setRight(fc)
    else:
        root.setLeft(fc)

    if child_queue.empty():
        return True
    
    sc = child_queue.front()
    if root.hasRight():
        if root.key() < sc.key():
            res1 = DFS(fc)
            if res1:
                return True
            else:
                return False
        else:
            return False
    elif root.hasLeft():
        if root.key() > sc.key():
            res1 = DFS(fc)
            if res1:
                return True
            else:
                return False
        else:
            return False
    


if __name__ == "__main__":

    line = list(map(int, input().split()))
    nodes = [BinaryTree(line[i]) for i in range(len(line))]
    
    child_queue = Queue()
    for i in range(1, len(line)):
        child_queue.push(nodes[i])
    root = nodes[0]

    way_pos = DFS(root)

    if way_pos:
        print("YES")
    else:
        print("NO")
