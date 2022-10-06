class Dequeue():
    def __init__(self):
        self.__arr = []
        self.__count = 0
    
    def insertFront(self,data):
        if self.__count >= 10:
            return -1
        self.__arr = [data] + self.__arr
        self.__count+=1
    
    def insertRear(self,data):
        if self.__count >= 10:
            return -1
        self.__arr.append(data)
        self.__count+=1
    
    def deleteFront(self):
        if self.__count == 0:
            print(-1)
            return
        self.__arr.pop(0)
        self.__count-=1
    
    def deleteRear(self):
        if self.__count == 0:
            print(-1)
            return
        self.__arr.pop(-1)
        self.__count-=1
    
    def getFront(self):
        if self.__count == 0:
            return -1
        return self.__arr[0]
    
    def getRear(self):
        if self.__count == 0:
            return -1
        return self.__arr[-1]
        



# Reading Input
t = [int(x) for x in input().split(' ')]
i = 0
A = Dequeue()
while(t[i] != -1):
    n = t[i]
    i+=1
    if n == 1:
        k = A.insertFront(t[i])
        if k == -1:
            print(k)
        i+=1
    elif n == 2:
        k = A.insertRear(t[i])
        if k == -1:
            print(k)
        i+=1
    elif n == 3:
        A.deleteFront()
    elif n == 4:
        A.deleteRear()
    elif n == 5:
        k = A.getFront()
        print(k)
    elif n == 6:
        k = A.getRear()
        print(k)
        