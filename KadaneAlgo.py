lst=[-2,10,3,-5,15,6]
current_max=lst[0]
global_max=lst[0]
for i in range(1,len(lst)):
    if(current_max < 0):
        current_max = lst[i]
    else:
        current_max+=lst[i]
    if(global_max < current_max):
        global_max = current_max
print(global_max)