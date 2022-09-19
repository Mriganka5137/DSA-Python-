def LastIndexB(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    output = LastIndexB(arr, x, si+1)
    if output != -1:
        return output
    else:
        if arr[si] == x:
            return si
        else:
            return -1

arr=[1,5,6,4,1,2,3,1]
print(LastIndexB(arr,1,0))