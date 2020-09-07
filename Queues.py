# Stacks mean First In First Out - FIFO
# Enqueue - add an item to the end of the line
# dequeue - remove an item from the front of the line

# everything that you wait in line for

from collections import deque # double ended queue

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
