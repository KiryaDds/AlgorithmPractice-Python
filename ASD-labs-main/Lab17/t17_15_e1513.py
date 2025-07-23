# Завдання 17.15 by  Янголь Ярослав / Комп. мех / 2 курс


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


def dfs(root, level, nodes):
    if level == len(nodes) or not nodes[level]:
        return

    left_child = nodes[level].pop(0)
    root.left_child = left_child
    dfs(left_child, level + 1, nodes)

    if level + 1 < len(nodes) and nodes[level + 1] and not level == 1:
        right_child = nodes[level + 1].pop(0)
        root.right_child = right_child
        dfs(right_child, level + 2, nodes)
    elif nodes[level]:
        right_child = nodes[level].pop(0)
        root.right_child = right_child
        dfs(right_child, level + 1, nodes)


if __name__ == "__main__":
    nodes = []
    h = 0

    while True:
        line = input().strip()
        if line[0] == "*":
            break

        leafs = [Node(ch) for ch in line]
        nodes.append(leafs)
        h += 1

    nodes.reverse()
    root = nodes[0][0]

    binary_tree = BinaryTree(root)
    dfs(root, 1, nodes)
    binary_tree.show(root)
