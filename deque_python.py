from collections import deque

# queue = deque(['name','age','DOB'])
# print(queue)

# de = deque([1,2,3])
# de.append(4)
# print(de)

# de.appendleft(5)
# print(de)

# de.pop()
# print(de)

# de.popleft()
# print(de)

# de = deque([1,2,3,3,4,6,7,8])
# # print(de.index(4,5,6))

# de.insert(4,3)
# print(de)

# print(de.count(4))

de = deque([1,2,3])
de.extend([4,5,6])
print(de)

de.extendleft([-2,-1,0])
print(de)

de.rotate(-3)
print(de)

de.reverse()
print(de)