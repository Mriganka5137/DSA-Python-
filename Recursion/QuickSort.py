def partition(a,si,ei):
    pivot = a[si]
    c=0
    for i in range(si+1,ei+1):
        if a[i] < pivot:
            c+=1
    a[si],a[si+c] = a[si+c],a[si]
    pivot_index = si+c
    i=si
    j=ei
    while(i<j):
        if a[i] < pivot:
            i+=1
        elif a[j] >= pivot:
            j-=1
        else:
            a[i],a[j] = a[j],a[i]
    return pivot_index

def quick_sort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index-1)
    quick_sort(a,pivot_index+1,ei)

a = [14,1,5,6,85,16,45,12]
print(partition(a,0,len(a)-1))
print(quick_sort(a,0,len(a)-1))