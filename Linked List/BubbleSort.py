from platform import node


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

def BubbleSort(head):
    n = length(head)
    for i in range (n -1):
        prev = None
        curr = head
        for j in range (n-i-1):
            if curr.data <= curr.next.data:
                prev = curr
                curr = curr.next
            else:
                if prev is None:
                    fwd = curr.next
                    head = head.next
                    curr.next = fwd.next
                    fwd.next = curr
                    prev = fwd
                else:
                    fwd = curr.next
                    prev.next = fwd
                    curr.next = fwd.next
                    fwd.next = curr
                    prev = fwd
    return head

node = InputLinkedList()
PrintLL(node)
node = BubbleSort(node)
PrintLL(node)