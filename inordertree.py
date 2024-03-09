## Inorder Traversal

class node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printInorder(root):

    if root:
        printInorder(root.left)

        print(root.data)

        printInorder(root.right)

if __name__ == "__main__":
	root = node(1)
	root.left = node(2)
	root.right = node(3)
	root.left.left = node(4)
	root.left.right = node(5)

	# Function call
	print("\nInorder traversal of binary tree is")
	printInorder(root)