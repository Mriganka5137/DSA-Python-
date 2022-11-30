import heapq

def kLargestEle(arr, k):
  heap = arr[:k]
  heapq.heapify(heap)

  for i in range(k, len(arr)):
    if arr[i] > heap[0]:
      heapq.heapreplace(heap, arr[i])
  
  return heap



arr = [2,12,9,16,10,5,3,20,25,11,1,8,6]
k = 4
ans = kLargestEle(arr, k)

for ele in ans:
  print(ele, end=" ")