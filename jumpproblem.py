def jump_problem(arr):
    n = len(arr)
    i = 0
    count = 0
    while i in arr:
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                count+=1
                i+=1
    return count+1

arr = [3,1,4,2,5,3]
n = len(arr)
jump_problem(arr)