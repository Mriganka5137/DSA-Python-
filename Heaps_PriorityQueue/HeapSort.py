def DownHeapify(arr, i, n):
  
  parentIndex = i
  leftChild = parentIndex * 2 + 1
  rightChild = parentIndex * 2 + 2

  # we will go down from index i to n to look for conditions
  while(leftChild < n):
    
    minIndex = parentIndex
    if(arr[minIndex] > arr[leftChild]):
      minIndex = leftChild
    
    if(rightChild < n and arr[minIndex] > arr[rightChild]):
      minIndex = rightChild

    if parentIndex == minIndex:
      return
    
    arr[minIndex], arr[parentIndex] = arr[parentIndex], arr[minIndex]

    parentIndex = minIndex
    leftChild = parentIndex * 2 + 1
    rightChild = parentIndex * 2 + 2
    


def HeapSort(arr):

  # We will only target the nodes which are not leaf nodes
  # (n//2 - 1) to 0 are not leaf nodes

  #This will create the CBT and satisfy min heap properties
  for i in range(n//2 - 1, -1, -1):
    DownHeapify(arr, i, n)

  
  for i in range(n-1, -1, -1):
    arr[0], arr[i] = arr[i], arr[0]
    DownHeapify(arr,0,i)
  


n = input()
arr = [int(ele) for ele in input().split()]
HeapSort(arr)
for ele in arr:
  print(ele, end=" ")