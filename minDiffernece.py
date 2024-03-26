# Naive Approch 
# def minDiff(arr):
#     n = len(arr)
#     res = arr[0]
#     for i in range(1,n-1):
#         for j in range(i):
#             res = min(res,abs(arr[i]-arr[j]))
#     return res
# arr = [5,3,8]
# print(f"number:",minDiff(arr))

# Efficient Approch

def minDiff(arr):
    n = len(arr)
    arr.sort()
    res = arr[0]
    for i in range(1,n):
        for j in range(i):
            res = min(res,abs(arr[i]-arr[j]))
    return res

arr = [5,3,8]
print(f"Number :",minDiff(arr))
