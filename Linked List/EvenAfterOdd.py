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

def evenAfterOdd(head) :
    if head is None:
        return head
    OddHead = None
    EvenHead = None
    even = None
    odd = None
    while(head is not None):
        if head.data % 2 == 0:
            if EvenHead is None:
                EvenHead = head
                even = EvenHead
                head = head.next
            else:
                even.next = head
                even = even.next
                head = head.next
        else:
            if OddHead is None:
                OddHead = head
                odd = OddHead
                head = head.next
            else:
                odd.next = head
                odd = odd.next
                head = head.next
    if EvenHead is None:
        return OddHead
    if OddHead is None:
        return EvenHead
    odd.next = EvenHead
    even.next = None
    return OddHead

node = InputLinkedList()
PrintLL(node)
node = evenAfterOdd(node)
PrintLL(node)