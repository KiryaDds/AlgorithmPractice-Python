# Завдання 17.6 by  Янголь Ярослав / Комп. мех / 2 курс


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
    
    def _show(self, root):
        print(root, end="")
        if root.hasNoChildren():
            return
        if root.hasLeft():
            root._show(root.mLeftChild)
        if root.hasRight():
            root._show(root.mRightChild)
        return
    
    def show(self):
        self._show(self)
    
    
def DFS(root, level):
    if level == h or len(nodes[level]) == 0:
        return
    
    left_child = nodes[level].pop(0)
    root.setLeft(left_child)
    DFS(left_child, level + 1)

    if level + 1 < h and len(nodes[level+1]) > 0 and not level == 1:
        right_child = nodes[level+1].pop(0)
        root.setRight(right_child)
        DFS(right_child, level + 2)
    elif len(nodes[level]) > 0:
        right_child = nodes[level].pop(0)
        root.setRight(right_child)
        DFS(right_child, level + 1)



if __name__ == "__main__":

    nodes = list()
    h = 0
   
    while True:

        line = input().strip().strip("\n")
        if line[0] == "*":
            break
        
        leafs = list()
        for i in range(len(line)):
            leafs.append(BinaryTree(line[i]))

        nodes.append(leafs)
        h += 1

    nodes.reverse()
    root = nodes[0][0]

    DFS(root, 1)
    root.show()
