arr1=[1,4,5,11,27]
arr2=[3,5,6,8,22,25]
arr=[]
n1=len(arr1)
n2=len(arr2)
i=0
j=0
k=0
while i < n1 and j < n2:
    if(arr1[i] < arr2[j]):
        arr.append(arr1[i])
        i+=1
    else:
        arr.append(arr2[j])
        j+=1
while (i < n1):
    arr.append(arr1[i])
    i+=1
while(j < n2):
    arr.append(arr2[j])
    j+=1
print(arr)
