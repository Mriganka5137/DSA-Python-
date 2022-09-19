a=[1,3,6,11,12,17]

d=3
i=0
j=6-1
while(i<=j):
    a[i],a[j] = a[j],a[i]
    i+=1
    j-=1
i=0
j=6-d-1
while(i<=j):
    a[i],a[j] = a[j], a[i]
    i+=1
    j-=1

i=6-d
j=6-1
while(i<=j):
    a[i],a[j] = a[j],a[i]
    i+=1
    j-=1
print(a)
