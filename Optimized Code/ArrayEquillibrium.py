def arrayEquilibrium(arr, n):
    sum = 0
    for ele in arr:
        sum+=ele
    leftside_sum = 0
    for i in range(n):
        if (leftside_sum == sum - arr[i] - leftside_sum):
            print(i)
            return
        leftside_sum+=arr[i]
    print("-1")
    return
arr=[2, 3, 10, -10, 4, 2, 9]
arrayEquilibrium(arr,7)