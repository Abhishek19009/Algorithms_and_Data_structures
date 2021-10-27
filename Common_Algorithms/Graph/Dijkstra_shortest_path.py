# Implementing Dijkstra

# Not working, fix the bug

import heapq as hp

class Node:
	def __init__(self, index, distance):		# We can also add extra properties of the node.
		self.index = index
		self.distance = distance

class Graph:
	def __init__(self, n): 		# n == no of nodes
		self.n = n
		self.adj = [[] for _ in range(n)]
		self.visited = [0 for _ in range(n)]
		self.nodeList = [None for _ in range(n)]
		self.pq = []

	def nodeInit(self, node):
		# Initialize the nodes in Graph
		# The distance is what we need to update. The shortest path to reach Node(6) would be corresponding distance.
		self.nodeList[node.index] = node

	def addEdge(self, u, v, path_cost):		# u, v corresponds to node index NOT distances!!
		self.adj[u].append((v, path_cost))		
	
	def dijkstra(self, start, dest):
		hp.heappush(self.pq, (self.nodeList[start].distance, start, 0))
		
		self.visited[start] = 1

		cur = (0, start, 0)

		while self.pq:
			print(cur)
			if cur[1] == dest:
				break

			prev_distance = cur[0]

			for neighbour in self.adj[cur[1]]:
				if not self.visited[neighbour[0]]:
					hp.heappush(self.pq, (self.nodeList[neighbour[0]].distance, neighbour[0], neighbour[1]))	
					# neighbour[0] = index, neighbour[1] = path_cost
					self.visited[neighbour[0]] = 1

			
			cur = hp.heappop(self.pq)

			if prev_distance + cur[2] < cur[0]:
				self.nodeList[cur[1]].distance = prev_distance + cur[2] 
			
		
		return self.nodeList[cur[1]].distance


if __name__ == "__main__":
	g = Graph(7)
	g.addEdge(0, 1, 2)
	g.addEdge(0, 2, 3)
	g.addEdge(1, 3, 4)
	g.addEdge(2, 4, 9)
	g.addEdge(3, 4, 8)
	g.addEdge(3, 5, 3)
	g.addEdge(4, 6, 7)

	g.nodeInit(Node(0, 0))
	g.nodeInit(Node(1, 2))
	g.nodeInit(Node(2, 3))
	g.nodeInit(Node(3, float("Inf")))
	g.nodeInit(Node(4, float("Inf")))
	g.nodeInit(Node(5, float("Inf")))
	g.nodeInit(Node(6, float("Inf")))


	print(g.dijkstra(0, 6))

	
