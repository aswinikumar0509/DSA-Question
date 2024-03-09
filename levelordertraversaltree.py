from collections import deque

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def levelOrder(root):

    if root is None:
        return
    q = deque()
    q.append(root)

    while len(q)>0:
        node = q.popleft()
        print(node.data, end = " ")
        if node.data is None:
            print("None",end = " ")

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

levelOrder(root)