# Queue - add and remove (worst case :- linear and linear)
# (best case :- constant and constant, use tail pointer to reduce complexity)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class QueueClass:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def add(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
        if self.tail.data is None:
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

# The above part is quite tricky.
# Remember that unless you are preserving the value of node in either self.head or
# self.tail you are not losing any node
# That's why
# self.tail.next = new_node
# self.tail = new_node
# works because the new_node was linked to self.head initially
# Hadn't there been any self.head, above command would not be possible

    def remove(self):
        remove_node = self.head
        self.head = self.head.next
        return remove_node.data

