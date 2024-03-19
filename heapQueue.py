import heapq

pq = [5,20,1,30,4]

heapq.heapify(pq)

# print(heapq.nlargest(2,pq))
# print(heapq.nsmallest(2,pq))

print(heapq.heappushpop(pq,2))
print(pq)
print(heapq.heappushpop(pq,0))
print(pq)
print(heapq.heapreplace(pq,-1))
print(pq)