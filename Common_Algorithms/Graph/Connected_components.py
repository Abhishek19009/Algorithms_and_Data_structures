class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(self.V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFSUtil(self, visited, temp, i):
        visited[i] = True

        temp.append(i)

        for v in self.adj[i]:
            if visited[v] == False:
                temp = self.DFSUtil(visited, temp, v)

        return temp

    def connectedComponents(self):
        visited = [False]*self.V
        cc = []
        for i in range(self.V):
            if visited[i] == False:
                temp = []
                cc.append(self.DFSUtil(visited, temp, i))

        return cc


# Driver Code

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)

print("Following are the connected Components: ", g.connectedComponents())
