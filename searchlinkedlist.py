class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

def print_list(head):
    curr = head
    while(curr!=None):
        print(curr.data , end=" ")
        curr = curr.next

def search_list(head,x):
    pos = 1
    curr = head
    while (curr!=None):
        if(curr.data==x):
            return pos
        pos+=1
        curr = curr.next
    return -1

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

search_list(head,50)
# print_list(head)