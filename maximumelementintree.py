## Finding the maximum element in the tree

class node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def findMax(root):

    if root is None:
        return float('-inf')
    
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)

    if(lres>res):
        res = lres
    if(rres>res):
        res = rres

    return res

if __name__ == '__main__':
	root = node(2)
	root.left = node(7)
	root.right = node(5)
	root.left.right = node(6)
	root.left.right.left = node(1)
	root.left.right.right = node(11)
	root.right.right = node(9)
	root.right.right.left = node(4)

	# Function call
	print("Maximum element is",
		findMax(root))