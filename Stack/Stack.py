class Stack:
    def __init__(self):
        self.__data = []
    
    # Push an element to Stack
    def push(self,item):
        self.__data.append(item)
    
    
    def pop(self):
        if self.isEmpty():
            return print("Your stack is already empty Babua")
 
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Your Stack is Empty Babua")
            return
        return self.__data[len(self.__data) -1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.__data)
        
s = Stack()
s.push(15)
s.push(21)
s.push(51)
while s.isEmpty() is False:
    print(s.pop())


    
