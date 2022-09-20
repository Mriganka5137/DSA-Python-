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

def printReverse(head) :
    if head is None:
        return
    if head.next is None:
        print(head.data,end=" ")
        return
    printReverse(head.next)
    print(head.data,end=" ")

def ReverseLL(head):
    prev = None
    current = head
    while(current is not None):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
node = InputLinkedList()
PrintLL(node)
# printReverse(node)
node = ReverseLL(node)
PrintLL(node)