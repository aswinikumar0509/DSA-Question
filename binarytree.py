class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


if __name__=='__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(4)