def MergeSort(li):
    if len(li) == 0 or len(li) == 1:
        return li
    mid=len(li)//2
    li1=li[0:mid]
    li2=li[mid:]
    MergeSort(li1)
    MergeSort(li2)
    index1=0
    index2=0
    index=0
    while(index1 < len(li1) and index2 < len(li2)):
        if(li1[index1] < li2[index2]):
            li[index]=li1[index1]
            index1+=1
            index+=1
        else:
            li[index]=li2[index2]
            index2+=1
            index+=1
    while(index1 < len(li1)):
        li[index]=li1[index1]
        index1+=1
        index+=1
    while(index2 < len(li2)):
        li[index]=li2[index2]
        index2+=1
        index+=1

li=[5,1,68,1,2]
MergeSort(li)
print(li)
