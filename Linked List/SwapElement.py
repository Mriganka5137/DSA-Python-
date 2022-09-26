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

def swapNodes(head, i, j) :
    if i == j:
        return head
    prev = None
    curr = head
    count = 0
    while(curr is not None):
        if count == i:
            prev1 = prev
            curr1 = curr
        if count == j:
            prev2 = prev
            curr2 = curr
        count+=1
        prev = curr
        curr = curr.next
    if prev1 is not None:
        prev1.next = curr2
    else:
        head = curr2
    if prev2 is not None:
        prev2.next = curr1
    else:
        head = curr1
    curr1.next , curr2.next = curr2.next , curr1.next
    return head
            
node = InputLinkedList()
PrintLL(node)
node = swapNodes(node,0,1)
PrintLL(node)