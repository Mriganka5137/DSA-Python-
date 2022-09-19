def UniqueElement(arr):
    merge_sort(arr)
    for i in range(0,len(arr)-1,2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return arr[len(arr)-1]
def merge_sort(arr):
    l = len(arr)
    if l == 0 or l ==1:
        return arr
    mid = l//2
    l1 = arr[:mid]
    l2 = arr[mid:]
    merge_sort(l1)
    merge_sort(l2)
    i = 0
    j = 0
    k = 0
    while(i < len(l1) and j < len(l2)):
        if(l1[i] < l2[j]):
            arr[k] = l1[i]
            k+=1
            i+=1
        else:
            arr[k] = l2[j]
            k+=1
            j+=1
    while(i < len(l1)):
        arr[k] = l1[i]
        k+=1
        i+=1
    while(j < len(l2)):
        arr[k] = l2[j]
        k+=1
        j+=1

def UniqueWithXor(arr,n):
    value = arr[0]
    for i in range(1,n):
        value = value ^ arr[i]
    return value

arr=[2,2,5,5,6,6,7]
print(UniqueElement(arr))
print(UniqueWithXor(arr,7))