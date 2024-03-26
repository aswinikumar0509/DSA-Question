# def kSmallest(arr,n,k):
#     arr.sort()
#     return arr[k-1]

# arr = [-2,3,54,45,32,0]
# A = kSmallest(arr,6,3)
# print(A)

# Efficient Approch

def partition(arr,l,r):
    x = arr[r]
    i = l
    for j in range(l,r):
        if(arr[j]<=x):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[i],arr[r] = arr[r],arr[i]
    return i

def kthSmallest(arr,k):
    l=0
    r = len(arr)-1
    while l<=r:
        p = partition(arr,l,r)
        if p==k-1:
            return p
        elif p>k-1:
            r = p-1
        else:
            l = p+1
    return -1

arr = [10,4,5,8,6,26]
k=5
print(kthSmallest(arr,k))
