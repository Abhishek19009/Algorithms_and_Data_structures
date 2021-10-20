# Topological sort implies sorting Directed Acyclic graphs(DAG) in Topological order.
# Method is not radically different and uses DFS as a subroutine.

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(self.v)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, i, at, vis, ordering):
        vis[at] = True

        for elem in self.adj[at]:
            if vis[elem] == False:
                i = self.dfs(i, elem, vis, ordering)

        ordering[i] = at
        return i - 1


    def topsort(self):
        vis = [False for i in range(self.v)]
        ordering = [0 for i in range(self.v)]
        i = self.v - 1

        for at in range(self.v):
            if vis[at] == False:
                i = self.dfs(i, at, vis, ordering)

        return ordering


g = Graph(5)
g.addEdge(0,1)
g.addEdge(2,3)
g.addEdge(2,1)
g.addEdge(4,1)
print(g.topsort())