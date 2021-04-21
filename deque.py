from collections import deque

queue = deque([1,2,3])

print(queue) # deque([1, 2, 3])

queue.popleft()

print(queue) # deque([2, 3])

queue.append(4)

print(queue) # deque([2, 3, 4])

queue.pop()

print(queue) # deque([2, 3])

queue.append(5)

print(queue) # deque([2, 3, 5])