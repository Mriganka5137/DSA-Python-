def checkFromLast(arr, x):
    l = len(arr)
    if l == 0:
        return -1
    
    output = checkFromLast(arr[1:], x)

    if output != -1:
        return output + 1
    else:
        if (arr[0] == x):
            return 0
        else:
            return -1

arr=[2,5,6,2,1,4]
print(checkFromLast(arr,5))