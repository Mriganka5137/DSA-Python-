def MaxProfit(arr):
    arr.sort()
    count=1
    maxCost = -1
    for i in range(len(arr)-1, -1, -1):
        currentCost = arr[i] * count
        if currentCost > maxCost:
            maxCost = currentCost
        count+=1
    return maxCost
arr = [34,15,90,78,67]
print(MaxProfit(arr))