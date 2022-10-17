def buildTree(preOrder, inOrder, n) :
  	#Your code goes here
    if len(preOrder) <=0:
        return None
    rootNode = preOrder[0]
    for i in range(n):
        if inOrder[i] == rootNode:
            break
    leftInOrder = inOrder[:i]
    rightInOrder = inOrder[i+1:]
    lengthOfLeft = len(leftInOrder)
    leftPreOrder = preOrder[1:lengthOfLeft+1]
    rightPreOrder = preOrder[lengthOfLeft+1:]
    
    root = BinaryTreeNode(rootNode)
    
    root.left = buildTree(leftPreOrder,leftInOrder,lengthOfLeft)
    root.right = buildTree(rightPreOrder, rightInOrder, n-lengthOfLeft)
    return root