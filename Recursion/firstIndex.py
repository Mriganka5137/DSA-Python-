def firstIndex(arr, x, start):
    l = len(arr)
    if l==0 or start == l:
        return -1
    if arr[start] == x:
        return start
    next = firstIndex(arr,x,start+1)
    return next

arr=[6,1,5,6,66,4,5,7]
x=6
print(firstIndex(arr,x,0))