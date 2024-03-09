
class node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def postorder(root):

    if root:

        postorder(root.left)
        postorder(root.right)
        print(root.data)

if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

# Function call
print( "\nPostorder traversal of binary tree is")
postorder(root)