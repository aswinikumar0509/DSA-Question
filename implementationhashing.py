class Myhash:

    def __init__(self,b):
        self.Bucket = b
        self.table = [[] for x in range(b)]

    def insert(self,x):
        i = x%self.Bucket
        self.table[i].append(x)

    def remove(self,x):
        i = x%self.Bucket
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self,x):
        i = x%self.Bucket
        return x in self.table[i]
    
h = Myhash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
