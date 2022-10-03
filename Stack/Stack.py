from ast import Expression


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
        
def isBalanced(expression) :
    s = Stack()
    for ele in expression:
        if ele == '(':
            s.push(ele)
        else:
            if s.top() != '(':
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False



expression = "(())"
if isBalanced(expression) :
	print("true")

else :
	print("false")
