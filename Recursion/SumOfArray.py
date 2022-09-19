def sum(arr):
    l = len(arr)
    if l==0:
        return 0
    if l==1:
        return arr[0]
    newArr = arr[1:]
    total = arr[0] + sum(newArr)
    return total

arr=[1,2,3,4,9]
print(sum(arr))