class myminHeap:

    def __init__(self):
        self.arr = []

    def parent(self,i):
        return (i-1)//2
    
    def lChild(self,i):
        return 2*i+1
    def rChild(self,i):
        return 2*i+2
    
    def insert(self,x):
        arr = self.arr
        arr.append(x)
        i = len(arr)-1

        while i>0 and arr[self.parent(i)]>arr[i]:
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i=p