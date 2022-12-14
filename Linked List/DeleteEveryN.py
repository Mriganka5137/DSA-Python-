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



def skipMdeleteN(head, M, N) :
    if head is None:
        return head
    curr = head
    while(head is not None):
        count = M - 1
        while(count > 0 and curr is not None):
            curr = curr.next
            count-=1
        if curr is None:
            return head
        remove = curr.next
        count = N
        while(count > 0 and remove is not None):
            remove = remove.next
            count-=1
        curr.next = remove
        curr = remove
    return head
node = InputLinkedList()
PrintLL(node)
node = skipMdeleteN(node,2,2)
PrintLL(node)
