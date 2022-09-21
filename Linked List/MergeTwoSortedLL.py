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


def mergeTwoSortedLinkedLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1 is None and head2 is None:
        return None
    finalHead = None
    finalTail = None
    if head1.data < head2.data:
        finalHead = head1
        finalTail = head1
        head1 = head1.next
    else:
        finalHead = head2
        finalTail = head2
        head2 = head2.next
    while(head1 is not None and head2 is not None):
        if head1.data < head2.data:
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next
        else:
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next
    if head1 is not None:
        finalTail.next = head1
    if head2 is not None:
        finalTail.next = head2
    return finalHead, finalTail

node1 = InputLinkedList()
node2 = InputLinkedList()
PrintLL(node1)
PrintLL(node2)
head, tail = mergeTwoSortedLinkedLists(node1, node2)
PrintLL(head)
