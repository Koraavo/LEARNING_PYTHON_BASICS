# Tree by the max number on the top
# height of tree is calculated from 1 going one level up

# max no of node = 7
# height = 2

# calculating nodes from height = [2**(height+1)] -1
# calculating height from nodes = floor(log height)
# calculating leaves in the end = [floor(nodes/2)+1] to total nodes

# Algorithm
# max_heapify(A, i) # A = array/list, i = index
# l = 2i
# r = 2i + 1
# if (l <= len(A) and A[l] > A[i]
    # largest = l
# else:
    # largest = i
# if (r <= len(A) and A[r] > A[largest]
    # largest = r
# if (largest != i)
    # Swap A[i], A[largest]
    # max-heapify(A, largest)

# build_max_heap(A):
# n = len(A)/2
# for i in range(n, -1, -1)
    # max_heapify(A, i)

# Example:
# a tree is so:
                # 11
        # 6               # 5
     # 0    # 8        # 2    # 7

# A = [11, 6, 5, 0, 8, 2, 7]
# nodes = len(A)
# leaves = [floor(nodes/2)+1] to nodes = 4, 5, 6, 7
# non-Leaf_nodes = 1, 2, 3
# first largest non_leaf_node = n = len(A)/2 = 3
# for i in range(3, -1, -1)
    # max_heapify(A, i)

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        # swap
        A[i], A[largest] =A[largest], A[i]
        max_heapify(A, largest)

def left(i):
    return (2*i) + 1

def right(i):
    return (2*i) + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(A, i)

# OR WITH CLASS

class Maxheap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap
        else:
            return False

    def pop(self):
        if len(self.heap) > 2: # check if the elements are more than two.
            self.__swap(1, len(self.heap)-1) # swap the first and the last item
            max = self.heap.pop() # pop the element
            self.__bubbleDown(1) # bubble down the element that was swapped and put in the first position
        elif len(self.heap) == 2: # otherwise, just get the max of the two numbers
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <=1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = (index * 2) + 1
        largest = index
        # if the item that is bubbling down is greater than the left child, swap
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)

m = Maxheap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
