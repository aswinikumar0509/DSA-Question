# Stack in python
# A stack is the linear data strucutre that store the value using LIFO data strucutre Last in First Out
# function associated with the stack
# empty()- Returns whethere the stack is empty - time complexity O(1)
# size()- Return the size of the stack - timeComplexity O(1)
# top() / peek() - Return the reference to the topmost element of the stack -  timeComplexity O(1)
# push(a) -  Insert the element in the top of the stack timeComplexity O(1)
# pop()- Delete the top most element of the stack - timeComplexity O(1)


stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack : ')

print(stack)

print('Stack after the element is poped : ')
print(stack.pop())
print(stack.pop())

print('Stack after the element is popped : ')
print(stack)



#  Implementation using the collections.deque:
# Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations.

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)