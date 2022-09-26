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
    MTail = None
    curr = head
    while(head is not None):
        count = 1
        while(count < M ):
            curr = curr.next
            count+=1
        MTail = curr
        count = 1
        while(count <= N and curr is not None):
            curr = curr.next
            count+=1
        MTail.next = curr
    return head
node = InputLinkedList()
PrintLL(node)
node = skipMdeleteN(node,2,2)
PrintLL(node)
