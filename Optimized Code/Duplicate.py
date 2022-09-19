def Duplicate(arr,n):
    sum = ((n-2)*(n-2+1))//2
    array_sum = 0
    for i in range(n):
        array_sum +=arr[i]
    return array_sum - sum
arr=[0,1,3,2,]
print(Duplicate(arr,5))