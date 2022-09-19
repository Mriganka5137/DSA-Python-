def check(arr,x):
    l = len(arr)
    if l == 0:
        return False
    if arr[0] == x:
        return True
    newArr = arr[1:]
    isPresent = check(newArr, x)
    return isPresent
arr=[5,6,8]
x=6
print(check(arr,x))