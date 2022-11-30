def checkMaxHeap(lst):
  n = len(lst)

  flag = True
  parentIndex = 0
  leftChild = 0 * 2 +1
  rightChild = 0 * 2 + 2
  while(leftChild < n):
    if(lst[leftChild] > lst[parentIndex]):
      flag = False
      return flag
    
    if rightChild >= n:
      break

    if(lst[rightChild] > lst[parentIndex]):
      flag = False
      return flag
    

    parentIndex += 1
    leftChild = parentIndex * 2 +1
    rightChild = parentIndex * 2 + 2

  return flag

lst = [42,20,18,6,14,11,51,4]
print(checkMaxHeap(lst))