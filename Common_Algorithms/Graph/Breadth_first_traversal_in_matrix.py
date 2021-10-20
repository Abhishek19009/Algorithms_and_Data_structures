# Direction Vectors
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def isValid(vis, row, col, obs):
    # If exceeded the boundary condiion
    if row < 0 or col < 0 or row > 3 or col > 3:
        return False

    # If visited already
    if vis[row][col] == True:
        return False

    # If present in obs
    if (row, col) in obs:
        obs.remove((row, col))
        vis[row][col] = True
        return False

    # Otherwise
    else:
        return True

def BFS(mat , vis, row, col, obs):
    queue = []

    queue.append((row, col))
    vis[row][col] = True

    while queue:
        cell = queue.pop(0)
        x = cell[0]
        y = cell[1]
        print(mat[x][y], end = " ")

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isValid(vis, adjx, adjy, obs):
                queue.append((adjx, adjy))
                vis[adjx][adjy] = True




if __name__ == "__main__":
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
           [13, 14, 15, 16]]

    # obstacle list
    obs = [(2,3), (1,2), (2,2), (3,2)]

    # Using 4x4 matrix for demonstration
    vis = [[False for i in range(4)] for i in range(4)]

    BFS(mat, vis, 0, 0, obs)
