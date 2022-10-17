def buildTree(postOrder, inOrder, n) :
  	#Your code goes here
    if n == 0:
        return None
    
    rootNode = postOrder[-1]
    root = BinaryTreeNode(rootNode)
    
    rootNodeIndex = -1
    for i in range(n):
        if inOrder[i] == rootNode:
            rootNodeIndex = i
            break
    
    leftInOrder = inOrder[:rootNodeIndex]
    rightInOrder = inOrder[rootNodeIndex + 1:]
    
    leftPostOrder = postOrder[:rootNodeIndex]
    rightPostOrder = postOrder[rootNodeIndex:-1]
    
    root.left = buildTree(leftPostOrder, leftInOrder, len(leftPostOrder))
    root.right = buildTree(rightPostOrder, rightInOrder, len(rightPostOrder))
    return root