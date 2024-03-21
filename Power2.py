def isPowerofTwo(n):

    if(n==0):
        return 0
    if(((n&(~(n-1))))==n):
        return 1
    return 0

n=4
print(isPowerofTwo(n))