class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def appendLastNToFirst(head, n) :
    if n == 0 or length(head) == 0:
        return head
    l = length(head)
    i=1
    firsthead = head
    while(head is not None):
        if(i == l - n):
            currentHead = head.next
            head.next = None
            i+=1
            break
        i+=1
        head = head.next
    head = currentHead
    while(head is not None):
        if(i == l):
            head.next = firsthead
            break
        i+=1
        head= head.next
    return currentHead

    


def length(head):
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count

def PrintLL(head):
    while head is not None:
        print(str(head.data) + "-->", end='')
        head = head.next
    print("None")
    return

def InputLinkedList():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for ele in inputList:
        if ele == -1:
            break
        newNode = Node(ele)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
def PrintLL(head):
    while head is not None:
        print(str(head.data) + "-->", end='')
        head = head.next
    print("None")
    return

newList = InputLinkedList()
PrintLL(newList)
print(length(newList))
head = appendLastNToFirst(newList, 0)
PrintLL(head)