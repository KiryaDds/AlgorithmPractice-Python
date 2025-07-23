class VertexBase:

    def __init__(self, key):
        self.mKey = key
        self.mData = None

    def key(self):
        return self.mKey

    def setData(self, data):
        self.mData = data

    def data(self):
        return self.mData


class Vertex(VertexBase):

    def __init__(self, key):
        super().__init__(key)
        self.mNeighbors = {}

    def addNeighbor(self, vertex, weight=1):
        if isinstance(vertex, VertexBase):
            self.mNeighbors[vertex.key()] = weight
        else:
            self.mNeighbors[vertex] = weight

    def neighbors(self):
        return self.mNeighbors.keys()

    def weight(self, neighbor):
        if isinstance(neighbor, VertexBase):
            return self.mNeighbors[neighbor.key()]
        else:
            return self.mNeighbors[neighbor]


class Graph:

    def __init__(self, oriented=False):
        self.mIsOriented = oriented
        self.mVertexNumber = 0
        self.mVertices = {}

    def addVertex(self, vertex):
        if vertex in self:
            return False
        new_vertex = Vertex(vertex)
        self.mVertices[vertex] = new_vertex
        self.mVertexNumber += 1
        return True

    def getVertex(self, vertex):
        assert vertex in self
        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.mVertices[key]

    def vertices(self):
        return self.mVertices

    def addEdge(self, source, destination, weight=1):
        if source not in self:
            self.addVertex(source)
        if destination not in self:
            self.addVertex(destination)
        self[source].addNeighbor(destination, weight)
        if not self.mIsOriented:
            self.mVertices[destination].addNeighbor(source, weight)

    def setData(self, vertex, data):
        assert vertex in self
        self[vertex].setData(data)

    def getData(self, vertex):
        assert vertex in self
        return self[vertex].data()

    def transpose(self):
        g_inv = Graph(self.mIsOriented)
        for vertex in self:
            for neighbor_key in vertex.neighbors():
                g_inv.addEdge(neighbor_key, vertex.key())
        return g_inv

    def __contains__(self, vertex):
        if isinstance(vertex, Vertex):
            return vertex.key() in self.mVertices
        else:
            return vertex in self.mVertices

    def __iter__(self):
        return iter(self.mVertices.values())

    def __len__(self):
        return self.mVertexNumber

    def __getitem__(self, vertex):
        return self.getVertex(vertex)


def DFS(graph, start):
    visited = set()
    __dfs_helper(graph, visited, start)
    return visited

def __dfs_helper(graph, visited, start):
    print(start, end=" ")
    visited.add(start)
    for neighbour in graph[start].neighbors():
        if neighbour not in visited:
            __dfs_helper(graph, visited, neighbour)