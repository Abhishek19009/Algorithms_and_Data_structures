'''
Tree traversal: Process of visiting ( checking or updating ) each node in  a tree
data structure one by one.

Unlike linked list which can only be traversed in linear order, trees can be traversed
in multiple order commonly via depth first order or breadth first order.

DEPTH - FIRST ORDER:-
Three ways to traverse in depth first order:-

In-order, Pre-order and Post-order

Binary tree is very large topic refer to binarytrees.pdf slide

'''


# In this case we are using list, but you can use your own implementation of
# stack and queue

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


# Overwriting python list to create Queue class for levelorder traversal( to define other features)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    def height(self, node=None):
        if node is None:
            return -1

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        return 1 + max(height_right, height_left)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            print(self.preorder_print(self.root, ""))
        elif traversal_type == "inorder":
            print(self.inorder_print(self.root, ""))
        elif traversal_type == "postorder":
            print(self.postorder_print(self.root, ""))
        elif traversal_type == "levelorder":
            print(self.levelorder_print(self.root))
        elif traversal_type == "reverse levelorder":
            print(self.reverse_levelorder_print(self.root))
        else:
            print("Traversal type " + traversal_type + " is not supported.")

    def size(self, node, size_count=0):
        if node:
            size_count += 1
            size_count = self.size(node.left, size_count)
            size_count = self.size(node.right, size_count)
        return size_count

    def is_bst_property_check(self):
        if self.root:
            is_satisfied = self._is_bst_property_check(self.root)
            if is_satisfied is None:  # is_satisfied will return either None or False
                return True
            return False
        return True

    def _is_bst_property_check(self, cur_node):
        if cur_node.left:
            if cur_node.value > cur_node.left.value:
                return self._is_bst_property_check(cur_node.left)
            else:
                return False
        if cur_node.right:
            if cur_node.value < cur_node.right.value:
                return self._is_bst_property_check(cur_node.right)
            else:
                return False


tree = BinarySearchTree(3)

tree.root.left = Node(2)
tree.root.right = Node(5)
tree.root.left.left = Node(1)
tree.root.left.right = Node(4)
tree.root.right.left = Node(4)
tree.root.right.right = Node(8)

# tree.print_tree("preorder")

# tree.print_tree("inorder")

# tree.print_tree("postorder")

# tree.print_tree("levelorder")

# tree.print_tree("reverse levelorder")

# print(tree.height(tree.root))
# print(tree.size(tree.root))

print(tree.is_bst_property_check())

random_tree = BinarySearchTree(3)
random_tree.root.left = Node(2)
random_tree.root.right = Node(5)
random_tree.root.left.left = Node(7)
random_tree.root.left.right = Node(10)

print(random_tree.is_bst_property_check())