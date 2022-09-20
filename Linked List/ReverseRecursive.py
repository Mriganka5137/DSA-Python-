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


# Best Time and Space Complexity
#Reverse a Linked List recursively
def reverseLinkedListRec(head) :
    if head is None or head.next is None:
        return head

    smallHead = reverseLinkedListRec(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

# O(n) Time Complexity
def reverseLinkedListRec2(head) :
    if head is None or head.next is None:
        return head, head

    smallhead, smalltail = reverseLinkedListRec2(head.next)
    smalltail.next = head
    head.next = None
    return smallhead, head


# O(n^2) Time Complexity
def reverseLinkedListRec3(head):
    if head is None or head.next is None:
        return head

    smallHead = reverseLinkedListRec3(head.next)
    curr = smallHead
    while(curr.next is not None):
        curr = curr.next
    curr.next = head
    head.next = None
    return smallHead


node = InputLinkedList()
PrintLL(node)
head, tail = reverseLinkedListRec2(node)
PrintLL(head)