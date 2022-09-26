class Stack:
    def __init__(self):
        self.__data = []
    
    # Push an element to Stack
    def push(self,item):
        self.__data.append(item)
    
    
    def pop(self,item):
        return self.__data.pop(item)
    
