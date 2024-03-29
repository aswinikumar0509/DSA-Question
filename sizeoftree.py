class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def size(node):
	if node is None:
		return 0
	else:
		return len(size(node.left)+ 1 + size(node.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Size of the tree is %d" %(size(root)))