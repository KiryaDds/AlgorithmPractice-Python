# Task e7463 by  Янголь Ярослав / Комп. мех. / 2 курс
# https://www.eolymp.com/uk/submissions/13890480


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
        print(root, end="-")
        if root.hasNoChildren():
            return
        if root.hasLeft():
            print(end="-l")
            root._show(root.mLeftChild)
        if root.hasRight():
            print(end="-r")
            root._show(root.mRightChild)
        return
    
    def show(self):
        self._show(self)



def Create_bt(root, nodes):

    if len(nodes) == 0:
        return
    
    if nodes[0] == bt.key():
        return
    
    if not root.hasLeft():
        if root.key() > nodes[0]:
            ch = BinaryTree(nodes.pop(0))
            root.setLeft(ch)
            Create_bt(ch, nodes)

    if len(nodes) == 0:
        return
    
    if not root.hasRight():
        if root.key() <= nodes[0]:
            ch = BinaryTree(nodes.pop(0))
            root.setRight(ch)
            Create_bt(ch, nodes)
            
    return


def _max_h(root, temp_h):
        
        global h
        temp_h += 1

        if root.hasNoChildren():
            if h > temp_h:
                h = temp_h
            temp_h = 0
            return
        if root.hasLeft():
            _max_h(root.mLeftChild, temp_h)
        if root.hasRight():
            _max_h(root.mRightChild, temp_h)
        return
    

def max_h(root):
    global h
    h = 1000
    _max_h(root, 0)
    return h
    
    

if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))

    bt = BinaryTree(nums.pop(0))
    Create_bt(bt, nums)

    #bt.show()
    print(max_h(bt))