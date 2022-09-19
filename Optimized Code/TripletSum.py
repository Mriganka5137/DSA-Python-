def TripletSum(arr,n,target):
    no_triplets = 0
    arr.sort()
    for i in range(n):
        pairTarget = target - arr[i]
        noPairs = PairSum(arr, i + 1, n-1, pairTarget)
        no_triplets += noPairs
    return no_triplets
def PairSum(arr, start, end, pairTarget):
    pairs = 0
    while(start < end):
        if(arr[start] + arr[end] > pairTarget):
            end-=1
        elif(arr[start] + arr[end] < pairTarget):
            start+=1
        else:
            startIndex = start
            startElement = arr[start]

            while(start<end and arr[start] == startElement):
                start+=1
            
            endIndex = end
            endElement = arr[end]

            while(end >= start and arr[end] == endElement):
                end-=1
            
            if(arr[startIndex] == arr[endIndex]):
                count = (start - startIndex) + (endIndex - end) -1
                pairs+=(count*(count+1))//2
            else:
                pairs+= (start- startIndex) * (endIndex - end)
    return pairs

arr = [1 ,2 ,3 ,4 ,5 ,6 ,7]
print(TripletSum(arr,7,12))