def intersection(arr1, arr2, n , m):
    merge_sort(arr1)
    print(arr1)
    merge_sort(arr2)
    print(arr2)
    i=0
    j=0
    while(i < n and j < m):
        # if(arr1[i] == arr2[j]):
        #     print(arr1[i],end=' ')
        #     i+=1
        #     j+=1
        # else:
        #     if(arr1[i] < arr2[j]):
        #         i+=1
        #     else:
        #         j+=1
        if(arr1[i] < arr2[j]):
            i+=1
        elif(arr1[i] > arr2[j]):
            j+=1
        else:
            print(arr1[i], end=' ')
            i+=1
            j+=1

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

# arr1 = [6,9,8,5]
# arr2 = [9,2,4,1,8]
# print(intersection(arr1,arr2,4,5))
    

