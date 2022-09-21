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


#Merge Sort
def MergeSort(head):
    if head.next is None:
        return head
    mid = MidPoint(head)
    secondHalf = mid.next
    mid.next = None
    head1 = MergeSort(head)
    head2 = MergeSort(secondHalf)
    head = mergeTwoSortedLinkedList(head1,head2)
    return head

#MidPoint Finder of Linked List
def MidPoint(head):
    if head is None or head.next is None:
        return head
    fast = head
    slow = head
    while(fast.next is not None and fast.next.next is not None):
        fast = fast.next.next
        slow = slow.next
    return slow

#Two Sorted Linked List Merging Function
def mergeTwoSortedLinkedList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    finalHead = None
    finalTail = None
    if(head1.data < head2.data):
        finalHead = head1
        finalTail = head1
        head1 = head1.next
    else:
        finalHead = head2
        finalTail = head2
        head2 =head2.next
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
    return finalHead

node = InputLinkedList()
head = MergeSort(node)
PrintLL(head)