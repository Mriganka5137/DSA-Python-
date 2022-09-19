def findTriplets(arr, n, k):
    arr.sort()
    ans=0
    for i in range(n-2):
        target = k - arr[i]
        left = i+1
        right = n-1
        while(left < right):
            if(arr[left] + arr[right] < target):
                left+=1
            elif(arr[left] + arr[right] > target):
                right-=1
            else:
                firstIndex  = left
                firstElement = arr[left]
                while(left < right and arr[left] == firstElement):
                    left+=1
                
                lastIndex = right
                lastElement = arr[right]
                while(right >= left and arr[right] == lastElement):
                    right-=1
                
                if(firstElement == lastElement):
                    equalNum = (left - firstIndex) + ( lastIndex - right) -1
                    ans+= (equalNum*(equalNum+1))//2
                else:
                    ans+= ((left- firstIndex)*(lastIndex - right))
    return ans