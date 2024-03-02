s1 = {10,20,30}
print(s1)

s2 = set([20,30,40])
print(s2)

s3 = {}

print('expected type set',type(s3))

s4 = set()

print(type(s4))

print(s4)


s = {10, 20}

s.add(30)

print(s)

s.add(30)  # adding duplicate items
print(s)

s.update([40, 50])

print(s)

s.update([60, 70], [80, 90])  # inserting multiple list

print(s)

s = {10, 30, 20, 40}

s.discard(30)

print(s)

s.remove(20)

print(s)

s.clear()

print(s)

s.add(50)

del s

s1 = {2, 4, 6, 8}

s2 = {3, 6, 9}

print('union ', s1 | s2)
print(s1.union(s2))

print('intersecton', s1 & s2)
print(s1.intersection(s2))

print('present in s1, but not present in s2', s1 - s2)
print(s1.difference(s2))

print('symmetric differences, not present in both', s1 ^ s2)

s1 = {2, 4, 6, 8}
s2 = {4, 8}

print('disjoint sets:', s1.isdisjoint(s2))

print('isSubset:', s1 <= s2)
print(s1.issubset(s2))

print('proper set:', s1 < s2)

print('s1 is superset of s2:', s1 >= s2)
print(s1.issuperset(s2))

print('s1 is proper superset of s2:', s1 > s2)