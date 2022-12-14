
from sys import stdin
from queue import Queue

class Stack :

  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()
    
  def getSize(self) :
    return self.q1.qsize()
  
  def isEmpty(self) :
    return self.getSize() == 0
    
  def push(self, data) :
    self.q1.put(data)
    return

  def pop(self) :
    if self.isEmpty():
      return -1
    while self.getSize() > 1:
      self.q2.put(self.q1.get())
    data = self.q1.get()
    
    temp = self.q1
    self.q1 = self.q2
    self.q2 = temp
    return data
  
  def top(self) :
		#Implement the top() function
    if self.isEmpty():
      return -1
    while self.getSize() > 1:
      self.q2.put(self.q1.get())
    data = self.q1.get()
    self.q2.put(data)
    
    temp = self.q1
    self.q1 = self.q2
    self.q2 = temp
    
    return data

		




#main
# 
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1