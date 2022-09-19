def BinarySearch(s,x,si,ei):
    if si > ei:
        return -1
    mid = (si+ei)//2
    if s[mid] == x:
        return mid
    elif s[mid] < x:
        return BinarySearch(s,x,mid+1,ei)
    else:
        return BinarySearch(s,x,si,mid-1)
print(BinarySearch([1,2,5,6,7,15,19],5,0,6)) 