# so a linked list has multiple nodes
# the front node is called as root node or Head
# each node consists of two things
    # value or data
    # and a pointer to the next data

# 3(data)-->(pointer)7-->10-->None
# Attributes:
# root is the pointer to the beginning of the list
# size

# Insertion of an element in singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert after a given node
    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node not in list")
            return

        # # if you keep on writing next to get to the next node
        # new_node = Node(data)
        # new_node.next = prev_node.next
        # prev_node.next = new_node

        # if you want to insert after a certain element
        cur_node = self.head
        while cur_node.data != prev_node:
            cur_node = cur_node.next

        prev_node = cur_node

        if not prev_node:
            print('Previous node is not in the list!')
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_with_element(self, key):
        # delete the head note
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data !=key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        current_node = self.head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        prev_pos = None
        count = 1
        while current_node and count !=pos:
            prev_pos = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        prev_pos.next = current_node.next
        current_node = None

    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        # Base case
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

llist = Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()
print(llist.len_recursive(llist.head))