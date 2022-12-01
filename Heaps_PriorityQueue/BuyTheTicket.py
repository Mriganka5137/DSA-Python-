import heapq as heap
class LinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.rear = None
    self.size = 0
  
  def enqueue(self, data):
    newNode = LinkedListNode(data)

    if self.head == None:
      self.head = self.rear = newNode
    else:
      self.rear.next = newNode
      self.rear = newNode
    self.size += 1
    return
  

  def dequeue(self):
    if self.head == None:
      return None
    
    data = self.head.data
    self.head = self.head.next
    self.size -= 1
    return data

  
  def getSize(self):
    return self.size

  def isEmpty(self):
    return self.size == 0
  
  def peek(self):
    if self.head is None:
      return None
    return self.head.data

def buyTicket(arr, n, k):
  q = Queue()
  maxHeap = []
  heap.heapify(maxHeap)

  for ele in arr:
    q.enqueue(ele)
    heap.heappush(maxHeap, -1*ele)
  
  count = 0

  while(len(maxHeap) != 0):
    if(q.peek() == -1* maxHeap[0]):

      if k == 0:
        return count + 1
      
      else:
        count += 1
        q.dequeue()
        heap.heappop(maxHeap)
        k -= 1
    
    else:
      q.enqueue(q.peek())
      q.dequeue()
      if k == 0:
        k = q.getSize() - 1

      else:
        k -= 1
  return count

