def printTwoOdd(arr,size):
    xor2 = arr[0]

    set_bit_no = 0
    n = size-2
    x,y = 0,0

    for i in range(1,size):
        xor2 = xor2 ^ arr[i]

    set_bit_no = xor2 & ~(xor2-1)

    for i in range(size):
        if(arr[i] & set_bit_no):
            x=x^arr[i]
        else:
            y = y^arr[i]
    print("The two ODD elements are", x, "&", y)

arr = [4, 2, 4, 5, 2, 3, 3, 1]
arr_size = len(arr)
printTwoOdd(arr, arr_size)
