class Queue():
  def __init__(self):
    self.__arr = []
    self.__front = 0
    self.__count = 0
  
  def enqueue(self,data):
    self.__arr.append(data)
    self.__count+=1
  
  def dequeue(self):
    if self.isEmpty():
      return "Queue is already empty"
    ele = self.__arr[self.__front]
    self.__front +=1
    self.__count-=1
    return ele

  def Front(self):
    if self.isEmpty():
      return "Queue is Empty Baba"
    return self.__arr[self.__front]
  
  def size(self):
    return self.__count
  
  def isEmpty(self):
    return self.size() == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
while(q.isEmpty() is False):
  print(q.Front())
  q.dequeue()
q.dequeue()