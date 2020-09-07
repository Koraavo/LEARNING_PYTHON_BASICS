# so a link list has multiple nodes
# the front node is called as root node
# each node consists of two things
# value or data
# and a pointer to the next data

# "3"-->"7"-->"10"
# Attributes:
# root is the pointer to the beginning of the list
# size

class Node:

    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedList:
    def __init__(self, head=None):
        self.head = head # the head is usually always the start
        self.len = 0

    # add method receives data, creates a new Node and pointer changes to the new node
    # increments size
    def append(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.len += 1


    # find iterates through the data and simply finds the data
    def find(self, data):
        this_node = self.head  # first node is the root node created by add method
        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return None

    # remove - removes data
    # requires prev_node and this_node
    # checks if it is in the root_node(first_node, prev_node is none)
    # bypass the deleted node
    def remove(self, data):
        this_node = self.head
        prev_node = None
        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:  # data is in the root
                    self.head = this_node.next_node
                self.len -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_list(self):
        this_node = self.head
        while this_node is not None:
            print(this_node, end='-->')
            this_node = this_node.next_node
        print('None')

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.len = 0

    # add method receives data, creates a new Node and pointer changes to the new node
    # increments size
    def append(self, data):
        if self.len == 0:
            self.head = Node(data)
        else:
            new_node = Node(data, self.head)
            self.head.next_node = new_node
        self.len += 1

    # find iterates through the data and simply finds the data
    def find(self, data):
        this_node = self.head  # first node is the root node created by add method
        while this_node is not None:
            if this_node.data == data:
                return data
            elif this_node.next_node == self.head:
                return False
            this_node = this_node.next_node

    # remove - removes data
    # requires prev_node and this_node
    # checks if it is in the root_node(first_node, prev_node is none)
    # bypass the deleted node
    def remove(self, data):
        this_node = self.head
        prev_node = None
        while True:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:  # data is in the root
                    while this_node.next_node != self.head:
                        this_node = this_node.next_node
                    this_node.next_node = self.head.next_node
                self.len -= 1
                return True
            elif this_node.next_node == self.head:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        this_node = self.head
        while this_node is not None:
            print(this_node, end='-->')
            this_node = this_node.next_node
        print('None')


myList = LinkedList()
myList.append(5)
myList.append(8)
myList.append(12)
myList.print_list()
print(myList.len)
