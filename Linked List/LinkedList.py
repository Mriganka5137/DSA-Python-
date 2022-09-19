from cgitb import small
from hashlib import new


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Following is the optimized Input for Linked List
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


# Print a Linked List

def PrintLL(head):
    while head is not None:
        print(str(head.data) + "-->", end='')
        head = head.next
    print("None")
    return



# Length of Linked List
def length(head):
    count=0
    while head is not None:
        count += 1
        head = head.next
    return count


# Print ith node of Linked List
def printIthNode(head, i):
    count = 0
    while(head is not None and count <= i):
        if i == count:
            print(head.data)
        count+=1
        head = head.next

#Insert at Position i
def InsertatI(head,i,n):
    if(i<0 or i > length(head)):
        return head
    count = 0
    prev = None
    current = head
    while(count < i):
        prev = current
        current = current.next
        count+=1
    newNode = Node(n)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = current
    return head

#delete at index i
def deleteNode(head, i) :
    if(i < 0 or i>=length(head)):
        return head
    count = 0
    prev = None
    current = head
    while(count < i):
        prev = current
        current = current.next
        count+=1
    if(prev is None):
        head = current.next
    else:
        prev.next = current.next
    return head

#length of Linked List Recursively
def lengthRecursive(head):
    if(head.next is None):
        return 1
    return 1 + lengthRecursive(head.next)


#Insert at ith index of Linked List recursively
def insertAtIth(head, i, data):

    if(i == 0):
        newNode = Node(data)
        newNode.next = head
        return newNode
    if(head is None or i< 0):
        return head
    small = insertAtIth(head.next, i-1, data)
    head.next = small
    return head


#Delete at index i recursively
def deleteNodeRec(head, pos) :
    if(head is None):
        return
    if (pos == 0):
        head = head.next
        return head
    smallHead = deleteNodeRec(head.next, pos-1)
    head.next = smallHead
    return head


newList = InputLinkedList()
PrintLL(newList)
print(lengthRecursive(newList))
# insertAtIth(newList, -3, 100)
deleteNodeRec(newList, 1)
PrintLL(newList)
# head = deleteNode(newList,41)
# PrintLL(head)
