'''
Single source shortest path algorithm (SSSP) used to calculate shortest path in Directed graph with negative edge weights.
This overcomes the limitation of Djikstra where we can calculate SSSP but only for graphs with no negative cycles.

Basically we try to calculate the minimum distance path for each node v - 1 times where v is number of vertices.
This stems from theorem that if graph has no negative cycles, we can calculate the shortest path after v - 1 times

Thus if we run algorithm again and we obtain decrease in distance, it implies that graph contains negative cycles.
'''

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex distance from Source")
        for i in range(self.v):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest path from src to all other vertices using Bellman-ford algorithm.
    # The function also detects the negative cycles.

    def BellmanFord(self, src):

        # Initialize distance from src to all other vertices INF
        dist = [float("Inf")]*self.v
        dist[src] = 0

        # Relax all edges v -1 times
        # A simple shortest path from src to any other vertex can have at most v - 1 edges

        for _ in range(self.v - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w


        # Checking whether graph has negative cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("The graph contains negative cycles.")
                return

        self.printArr(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(2, 3, 10)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.BellmanFord(0)



