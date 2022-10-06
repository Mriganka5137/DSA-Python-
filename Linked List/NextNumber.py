## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def ReverseLL(head):
  curr = head
  prev = None
  while curr is not None:
    fwd = curr.next
    curr.next = prev
    prev = curr
    curr = fwd
  return prev


def nextNumber(head):
    
    RevHead = ReverseLL(head)
    curr = RevHead
    carry = 1
    prev = None
    while(curr is not None):
        data = (curr.data + carry)%10
        carry = (curr.data + carry)//10
        curr.data = data
        prev = curr
        curr = curr.next
    if carry != 0 :
        newNode = Node(carry)
        prev.next = newNode
        newNode.next = None
    head = ReverseLL(RevHead)
    return head
        
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)