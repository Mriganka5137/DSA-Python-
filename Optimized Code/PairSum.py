def PairSum(arr, n ,target):
    arr.sort()
    i = 0
    j = len(arr) -1
    ans=0
    while(i < j):
        if(arr[i] + arr[j] < target):
            i+=1
        elif(arr[i] + arr[j] > target):
            j-=1
        else:
            startElement = arr[i]
            startIndex = i
            
            while(i<j and arr[i] == startElement):
                i+=1
            
            lastElement = arr[j]
            lastIndex = j
            while(j>=i and arr[j] == lastElement):
                j-=1
            
            if arr[startIndex] == arr[lastIndex]:
                count = (i - startIndex)+(lastIndex - j)-1
                ans+= (count *(count+1))//2
            else:
                ans+=(i-startIndex)*(lastIndex - j)
    return ans
arr = [1 ,3, 6, 2, 5, 4, 3, 2, 4]
print(PairSum(arr,9,5))