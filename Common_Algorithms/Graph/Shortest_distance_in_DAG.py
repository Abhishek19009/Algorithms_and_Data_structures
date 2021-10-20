# Shortest distance in a DAG could be found by using topological sort.
# Time complexity - O(V + E) which is best we can obtain.

# We initialize distances to all vertices as infinite and distance to source as 0, then we find topological sorting
# of the graph.
# Once we have the topological order, we one by one process all the vertices in topological order.
# For every vertex being processed, we update distances of its adjacent by comparing the distances.

from collections import defaultdict 

class Graph:
    def __init__(self, v):      # -> v represents number of vertices
        self.v = v
        self.graph = defaultdict(list)

    # function to add edge in the graph
    def addEdge(self, u, v, w):
        self.graph[u].append((v,w))

    def TopSort(self, v, visited, stack):
        visited[v] = True

        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.TopSort(node, visited, stack)

        stack.append(v)

    def shortestPath(self, s):
        visited = [False]*self.v
        stack = []

        # Call the recursive helper function to store the topological sort from source vertex.

        self.TopSort(s, visited, stack)

        # Initialize distances to all vertices as infinity
        # distance of source from itself will be 0
        dist = [float("Inf")] * self.v
        dist[s] = 0

        # Process vertices in topological order
        while stack:
            # Get the next vertex from topological order
            i = stack.pop()

            # Update distances of all the adjacent vertices
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        # printing the calculated shortest distances
        for i in range(self.v):
            print(dist[i], end= " ")

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

s = 1

g.shortestPath(s)



