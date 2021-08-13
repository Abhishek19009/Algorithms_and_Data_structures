'''
Height of node in binary tree is number of edges in longest path
between that node and leaf of tree.

Height to tree is height of its root node.
'''


def height(self, node=None):
    if node is None:
        return -1

    height_left = self.height(node.left)
    height_right = self.height(node.right)

    return 1 + max(height_right, height_left)