class Graph():
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(self.v)]
        self.visited = [False] * self.v

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFSUtil(self, node):
        self.visited[node] = True

        print(node, end=" ")

        for i in self.adj[node]:
            if self.visited[i] == False:
                self.DFSUtil(i)

        return None

    def DFS(self, i):  # i is starting root for DFS
        self.visited[i] = True

        print(i, end=" ")

        for elem in self.adj[i]:
            if self.visited[elem] == False:
                self.DFSUtil(elem)


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)

g.DFS(4)
