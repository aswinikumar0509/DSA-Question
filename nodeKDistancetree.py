class node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def Kdistance(root,k):
    if (root is None):
        return 
    if (k==0):
        print(root.data,end = " ")
    else:
        Kdistance(root.left,k-1)
        Kdistance(root.right,k-1)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(8)

Kdistance(root,2)