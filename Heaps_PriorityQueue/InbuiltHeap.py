import heapq


#Min Heap
# li = [5,6,1,5,9,78]

# heapq.heappush(li,55)
# print(heapq.heappop(li))
# heapq.heapreplace(li,100)
# print(li)


#Max Heap

arr = [1,2,3,4,5,6,7]
heapq._heapify_max(arr)
print(arr)

heapq._heapreplace_max(arr,0)
print(arr)

# print(heapq._heappop_max(arr))
# print(arr)

# arr.append(1000)
# print(arr)

# heapq._siftdown_max(arr, 0, len(arr) - 1)
# print(arr)