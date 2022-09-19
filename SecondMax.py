a=[4,2,1,5,0]
max=a[0]
secondMax=0
for i in range(1,len(a)):
    if a[i] > max:
        secondMax=max
        max=a[i]
    else:
        if(a[i]>secondMax):
            secondMax=a[i]
print(secondMax)
