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

def findNodeRec(head, n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    output = findNodeRec(head.next, n)
    if output == -1:
        return -1
    else:
        return 1 + output

node = InputLinkedList()
PrintLL(node)
print(findNodeRec(node,5))