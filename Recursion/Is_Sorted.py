from operator import truediv


def sorted(a):
    l = len(a)
    if l==0 or l==1:
        return True
    if a[0] > a[1]:
        return False

    smallerList = a[1:]
    isSmallerListSorted = sorted(smallerList)
    return isSmallerListSorted

def sortedBetter(arr,start):
    l = len(arr)
    if start == l-1 or start ==l:
        return True
    if arr[start] > arr[start+1]:
        return False
    isSorted = sortedBetter(arr,start+1)
    return isSorted

a=[1,2,3,5,7,9,11,25]
print(sorted(a))
print(sortedBetter(a,0))