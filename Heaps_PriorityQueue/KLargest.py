import heapq
def kthLargest(arr, k):
  heapq._heapify_max(arr)


  for i in range(k-1):
    heapq._heappop_max(arr)
  
  ele = heapq.heappop(arr)

  return ele



arr = [87, 79, 67 ,15 ,68, 68, 58, 89, 85, 30]
k = 9
ans=kthLargest(arr, k)
print(ans)