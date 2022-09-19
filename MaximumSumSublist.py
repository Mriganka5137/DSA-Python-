lst=[-2,10,7,-5,15,6]
max=0
n=len(lst)
for i in range(n):
    sum=lst[i]
    for j in range(i+1,n):
        sum+=lst[j]
        if(sum > max):
            max=sum

print(max)