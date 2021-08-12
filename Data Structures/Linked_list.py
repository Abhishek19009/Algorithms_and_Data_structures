class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# REMEMBER:- In all operations, we have to ensure that we don't break
# pointer chain because that's the essence of linked list.
# It's all about connecting of the pointers
# # Rather than creating LinkedList object with
# head value to be none we can pass head
# as instance variable i.e new_list = LinkedList(number)

class LinkedList:
    def __init__(self, head_data):
        self.head = Node(head_data)

    # Takes linear time to append at the end but if we pass the pointer
    # to the previous node, we can perform this operation in constant time

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    # push inserts data at the front
    # simple 3 step process, time complexity = O(1)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Time complexity of InsertAfter is O(1), thus if we have info of prevNode
    # we can add new node in O(1) complexity

    def InsertAfter(self, prevNode, data):
        if prevNode is None:
            print("Given prev Node must be in linked list.")

        new_node = Node(data)
        # This next step is very necessary, because we might be
        # inserting the node in the middle of list which will break chain
        # of pointers.
        new_node.next = prevNode.next
        prevNode.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of the range!!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


