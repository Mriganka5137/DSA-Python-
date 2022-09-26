from turtle import update


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


def kReverse(head, k) :
    curr, prev, next = head, None, None
    count = 0
    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count+=1
    if next is not None:
        head.next = kReverse(next, k)
    return prev







def Reverse(head):
    if head is None or head.next is None:
        return head
    curr = head
    fwd = None
    prev = None
    while curr is not None:
        fwd = curr.next
        curr.next = prev
        prev = curr
        curr = fwd
    return prev






node = InputLinkedList()
PrintLL(node)
node = kReverse(node,3)
PrintLL(node)
