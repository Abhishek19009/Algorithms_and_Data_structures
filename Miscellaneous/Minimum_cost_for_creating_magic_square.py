'''
Conditions:- Input matrix must be 3x3
Input elements must lie between 1 to 9

Properties of 3x3 magic square:-
middle element is 5
sum of elements in rows, column and diagnol is 15
All elements are distinct.
To form an algorithm which has less time complexity we need
to know at least 1  3x3 magic square.

Be careful:- Deep copy is used here to add matrices into new matrix
'''
import copy

mat = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
mg_sq_list = []


# Principle:- Once we know 1 magic square others can be derived from it
# via rotation and flipping
# A 3x3 matrix can be rotated 4 times and for each rotation we can flip the matrix
# So that accounts for 4(rotation) + 4(flipping) = 8 possible square matrix

def rotation():
    N = 3
    # Each cycle
    for x in range(0, int(N / 2)):
        # Rotating each 2x2 square
        for y in range(x, N - x - 1):
            # Storing Top-right to temporary variable
            temp = mat[x][y]

            # Top-right element assigned Top-left
            mat[x][y] = mat[y][N - x - 1]

            # Top-left is assigned Bottom-left
            mat[y][N - x - 1] = mat[N - x - 1][N - y - 1]

            # Bottom-left assigned Bottom-right
            mat[N - x - 1][N - y - 1] = mat[N - y - 1][x]

            # Bottom-right element assigned Top-right
            mat[N - y - 1][x] = temp


def flip():
    for i in range(len(mat)):
        temp = mat[i][len(mat) - 1]
        mat[i][len(mat) - 1] = mat[i][0]
        mat[i][0] = temp


def find_all_mg():
    for _ in range(4):
        temp = copy.deepcopy(mat)
        mg_sq_list.append(temp)
        rotation()

    for _ in range(4):
        flip()
        temp = copy.deepcopy(mat)
        mg_sq_list.append(temp)
        rotation()

find_all_mg()

# Inputs

my_matrix = []

for _ in range(3):
    input_list = list(map(int, input().rstrip().split()))

    my_matrix.append(input_list)

cost = 0
comp_list = []
for element in mg_sq_list:
    for i in range(3):
        for j in range(3):
            cost += abs(element[i][j] - my_matrix[i][j])
    comp_list.append(cost)
    cost = 0

# Output

print(min(comp_list))