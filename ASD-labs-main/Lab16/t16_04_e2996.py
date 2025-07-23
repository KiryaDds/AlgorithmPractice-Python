# Завдання 16.4 by  Янголь Ярослав / Комп. мех / 2 курс


class Node:
    
    def __init__(self, key):
        self.mKey = key

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def __str__(self):
        return str(self.mKey)


class Tree(Node):

    def __init__(self, key):
        super().__init__(key)
        self.mChildren = []

    def addChild(self, child):
        self.mChildren.append(child)

    def removeChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                self.mChildren.remove(child)
                return True
        return False

    def getChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.mChildren


    def DFS(self, current):

        global min_bribe

        current += bribes[self.key()]
        for child in self.getChildren():
            child.DFS(current)

        if current < min_bribe and len(self.getChildren()) == 0:
            min_bribe = current
        current -= bribes[self.key()]
        return

    
if __name__ == "__main__":

    n = int(input())
    placemans = [Tree(i) for i in range(n)]
    global min_bribe
    bribes = []
    
    for i in range(n):

        data = list(map(int, input().split()))
        bribes.append(data[0])
        for j in range(data[1]):
            placemans[i].addChild(placemans[data[j+2]-1])


    min_bribe = 100 * 100
    placemans[0].DFS(0)
    print(min_bribe)
