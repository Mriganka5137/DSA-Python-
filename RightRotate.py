lst=[10,20,30,40,50]
k=4
l=len(lst)
for i in range(k):
    temp=lst[l-1]
    index=l-1
    while(index > 0):
        lst[index]=lst[index-1]
        index=index-1
    lst[0]=temp
print(lst)