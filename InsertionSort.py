arr=[5,8,2,24,7,1]
n = len(arr)
for i in range(1,n):
    temp = arr[i]
    j = i-1
    while(j >=0 and temp < arr[j]):
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = temp
print(arr)