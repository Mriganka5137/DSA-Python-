lst = [1,2,3,4,5]
result=[]
for i in range(len(lst)//2):
    result.append(lst[-(i+1)])
    result.append(lst[i])
if len(lst)%2==1:
    result.append(lst[len(lst)//2])
print(result)