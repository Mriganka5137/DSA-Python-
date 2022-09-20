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

def PrintLL(head):
    while head is not None:
        print(str(head.data) + "-->", end='')
        head = head.next
    print("None")
    return

def removeDuplicates(head) :
    if head is None:
        return head
    prev = head
    current = head.next
    while(current is not None):
        if(prev.data != current.data):
            prev.next = current
            prev = current
            current = current.next
        else:
        	current = current.next
    prev.next = None   #Make sure to end the LL with a None value at the end node
    return head
def removeDuplicatesBetter(head) :
    if head is None:
        return head
    current  = head
    while(current.next is not None):
        if(current.data == current.next.data):
            current.next = current.next.next
        else:
            current =current.next
    return head
node = InputLinkedList()
PrintLL(node)
head = removeDuplicatesBetter(node)
PrintLL(head)