## Depth of the node

class node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def maxDepth(root):

    if root is None:
        return 0
    
    lDepth = maxDepth(root.left)
    rDepth = maxDepth(root.right)

    if(lDepth>rDepth):
        return lDepth+1
    else:
        return rDepth+1
    
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)


print("Height of tree is %d" % (maxDepth(root)))
    