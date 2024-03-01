class Node:

    def __init__(self,k):
        self.key = k
        self.next = None

def print_list(head):
    curr = head
    while(curr!=None):
        print(curr.key,end = "->")
        curr = curr.next
    
# temp1 = Node(10);
# temp2 = Node(30);
# temp3 = Node(20);
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print_list(head)
