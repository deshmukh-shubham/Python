# Try out the Python queue functions
# FIFO - FIRST IN FIRST OUT

from collections import deque

# TODO: Create a new empty deque object that will function as a queue
queue = deque() 

# TODO: Push items onto the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO: Print the queue contents
print(queue)

# TODO: Pop an item off the queue
x = queue.popleft()
print(x)
print(queue)
