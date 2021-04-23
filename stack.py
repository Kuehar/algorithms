# Stack is LIFO,Last In First Out data structure.

stack = [3,4,5]
print(stack) # [3,4,5]
stack.append(6)
print(stack) # [3,4,5,6]
stack.append(7)
print(stack) # [3,4,5,6,7]

stack.pop()
print(stack) # [3,4,5,6]

stack.pop()
print(stack) # [3,4,5]


class Stack:
    def init(self):
        