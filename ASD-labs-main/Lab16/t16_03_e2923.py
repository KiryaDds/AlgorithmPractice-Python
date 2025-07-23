# Завдання 16.3 by  Янголь Ярослав / Комп. мех / 2 курс


class Node:
    
    def __init__(self, key):
        self.mKey = key

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def __str__(self):
        return str(self.mKey)


class UnorderedTree(Node):

    def __init__(self, key):
        super().__init__(key)
        self.mChildren = {}

    def addChild(self, child):
        self.mChildren[child.key()] = child

    def removeChild(self, key):
        if key in self.mChildren:
            del self.mChildren[key]
            return True
        else:
            return False

    def getChild(self, key):
        if key in self.mChildren:
            return self.mChildren[key]
        else:
            return None

    def getChildren(self):
        return self.mChildren.values()
    
    def DFS(self, color):

        current = set([color[self.key()]])
        for child in self.getChildren():
            t = child.DFS(color)

            if len(current) < len(t):
                current, t = t, current
            current = current.union(t)
        
        numofcolors[self.key()] = len(current)
        return current


if __name__ == "__main__":

    n = int(input())
    nodes = [UnorderedTree(i) for i in range(n)]
    color = []
    
    for i in range(n):
        p, c = map(int, input().split())
        color.append(c)
        if p == 0:
            root = nodes[i]
        else:
            nodes[p-1].addChild(nodes[i])
    
    numofcolors = [0 for i in range(n)]

    root.DFS(color)

    for i in range(n):
        print(numofcolors[i], end=" ")
