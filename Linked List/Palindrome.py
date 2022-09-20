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

def length(head):
    count=0
    while head is not None:
        count += 1
        head = head.next
    return count

def ReverseLL(head):
    fwd = None
    prev = None
    currn = head
    while(currn is not None):
        fwd = currn.next
        currn.next = prev
        prev = currn
        currn = fwd
    return prev

def Palindrome(head):
    if head is None or head.next is None:
        return True
    fast = head
    slow = head
    while(fast.next is not None and fast.next.next is not None):
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None
    second = ReverseLL(second)
    

    #compare
    firstList = second
    secondList = head
    while(firstList is not None):
        if(firstList.data != secondList.data):
            return False
        firstList = firstList.next
        secondList = secondList.next
    return True





node = InputLinkedList()
PrintLL(node)
print(Palindrome(node))
    


