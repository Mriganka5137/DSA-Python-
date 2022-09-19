def mergeSort(li):
    # Please add your code here
    if len(li) == 0 or len(li) == 1:
        return li
    mid=len(li)//2
    li1=li[0:mid]
    li2=li[mid:]
    li1 = mergeSort(li1)
    li2 = mergeSort(li2)
    #output=[]
    index1=0
    index2=0
    index=0
    while(index1 < len(li1) and index2 < len(li2)):
        if(li1[index1] < li2[index2]):
            li.insert(index,li1[index1])
            index1+=1
            index+=1
        else:
            li.insert(index,li2[index2])
            index2+=1
            index+=1
    while(index1 < len(li1)):
        li.insert(index,li1[index1])
        index1+=1
        index+=1
    while(index2 < len(li2)):
        li.insert(index,li2[index2])
        index2+=1
        index+=1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(arr)