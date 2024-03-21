# def countsetbits(n):
#     res = 0
#     while n:
#         if n%2==1:
#             res = res+1
#         n = n//2
#     return res

# n=5

# print(countsetbits(n))


# better way to do the same

def countsetBit(n):

    count = 0 
    while n:
        n = n&(n-1)
        count+=1
    return count

n=5
print(countsetBit(n))