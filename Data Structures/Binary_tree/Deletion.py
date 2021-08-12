'''
Deletion in binary tree is most tricky in terms of code implementation
So keep coming and revising the concepts.

Always if performing somewhat complex recursion or if you are not sure
whether algorithm will work, try to break main methods in two different methods
ex - in this case we used "deleteNode" method as main calling method
and "_deleteNode" is used to do dirty work of recursion.


Remember the basic concept:
To delete node having left or right child we need to replace either by rightmost
of left child or leftmost of right child.
Also after every deletion operation, corresponding node should be updated
ex- if we are deleting 5, after deletion operation is done we need to update
right child of 2 to be the modified node .
This is done by including "return node" at end of function.

Special case to consider:- If tree only contain one node( root node) we have to
manually delete the node.
We have a advantage here because we already splitted the methods in two
parts "deleteNode" and "_deleteNode"
Thus hard code deletion of root only case is done in "deleteNode" method.

Ex-  in   2
            /   \
            1       5
        /   \       /   \
    0.5     1.5   3     7
                    /   \
                   2.5  4

    in order to delete node 5, we would consider performing

'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, ):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print("Duplicate datas are not allowed.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return False

    def _find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)

        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

        elif data == cur_node.data:
            return True

    def inorder_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def deleteNode(self, key):
        if not self.find(key):
            print("No such element found in the tree!!!")
        if self.root is None:
            return "The tree is empty!!"

        if not self.root.left and not self.root.right:
            self.root = None
            print("All nodes deleted!")
            return None

        self._deleteNode(self.root, key, prime_key=key)

    def _deleteNode(self, node, key, prime_key):
        if node.data < key:
            if node.right:
                node.right = self._deleteNode(node.right, key, prime_key=prime_key)

        elif node.data > key:
            if node.left:
                node.left = self._deleteNode(node.left, key, prime_key=prime_key)

        else:
            if node.right:
                pnt = node.right
                while pnt.left:
                    pnt = pnt.left
                node.data = pnt.data
                node.right = self._deleteNode(node.right, node.data, prime_key=prime_key)

            elif node.left:
                pnt = node.left
                while pnt.right:
                    pnt = pnt.right
                node.data = pnt.data
                node.left = self._deleteNode(node.left, node.data, prime_key=prime_key)

            elif not node.right and not node.left:
                node = None
                print("Node {} is successfully deleted!!!".format(prime_key))

        return node


bst = BST()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

# print(bst.find(4))
# print(bst.find(8))
# print(bst.find(10))
# print(bst.find(12))


bst.deleteNode(8)
bst.deleteNode(7)