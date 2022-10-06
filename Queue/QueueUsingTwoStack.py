class queueUsing2Stack:
  def __init__(self):
    self.s1=[]
    self.s2=[]

  def enqueue(self,data):
    self.s1.append(data)
  

  def dequeue(self):
    while len(self.s1) == 1:
      self.s2.append(self.s1.pop())
    data = self.s1.pop()

    while len(self.s2) == 0:
      self.s1.append(self.s2.pop())
    return data

q = queueUsing2Stack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

