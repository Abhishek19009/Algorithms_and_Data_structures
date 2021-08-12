# Stack:- push and pop

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class StackClass:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def push(self, data):
        new_node = Node(data)
        if self.tail.data and self.head.data is None:
            self.tail = new_node
            self.head = new_node
            return None

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        pop_value = self.head.data
        self.head = self.head.next
        return pop_value


new_stack = StackClass()


new_stack.push(12)
new_stack.push(20)
new_stack.push(50)

