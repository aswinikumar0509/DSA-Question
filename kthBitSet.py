# Check whether the K-th bit is set or not Using Left Shift Operator:
# To solve the problem follow the below idea:

# Left shift given number 1 by k-1 to create a number that has only 
# set bit as k-th bit.
# temp = 1 << (k-1)
# If bitwise AND of n and temp is non-zero, then result is SET else 
#  result is NOT SET

def isKthBitSet(n,k):
    if n&(1<<(k-1)):
        print("Set")
    else:
        print("Not Set")

n=5
k=1
isKthBitSet(n,k)