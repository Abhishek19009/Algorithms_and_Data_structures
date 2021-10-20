# Implementing BFS to calculate shortest distance

class Node:
    def __init__(self, x, y, dist, path):
        self.x = x
        self.y = y
        self.dist = dist
        self.path = path


def isValid(row, col, visited, obs):
    if row < 0 or col < 0 or row > 3 or col > 3:
        return False

    if visited[row][col] == True:
        return False

    if (row, col) in obs:
        obs.remove((row, col))
        visited[row][col] = True
        return False

    else:
        return True

def BFS(grid, visited, rows, cols, rowe, cole, obs):
    dRow = [1, 0, -1, 0]
    dCol = [0, -1, 0, 1]

    queue = []

    if rowe == rows and cole == cols:
        return "Destination is same as the source!!!"

    queue.append(Node(rows, cols, 0, f"({rows}, {cols}) -> "))
    visited[rows][cols] = True

    while queue:
        popped = queue.pop(0)
        x = popped.x
        y = popped.y
        dist = popped.dist
        path = popped.path

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if isValid(adjx, adjy, visited, obs):
                if adjx == rowe and adjy == cole:
                    print(path + f"({adjx}, {adjy})")
                    return "Shortest distance is " + str(dist + 1)

                queue.append(Node(adjx, adjy, dist+1, path + f"({adjx}, {adjy}) -> "))
                visited[adjx][adjy] = True


# Driver Code

if __name__ == '__main__':
    visited = [[False for i in range(4)] for i in range(4)]

    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
            [13, 14, 15, 16]]

    obs = [(2, 3), (1, 2), (2, 2), (3, 2)]

    result = BFS(grid, visited, 0, 0, 1, 3, obs)
    print(result)
