def findNode(head, n) :
    if head is None:
        return -1
    if head.data == n:
        return 0
    else:
        index = findNode(head.next, n)
        if index == -1:
            return -1
        else:
            return 1 + index
