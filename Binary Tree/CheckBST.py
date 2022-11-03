from turtle import right


def checkBST(root):
  if root is None:
    return True

  maxLeft = maxNodeValueInTree(root.left)
  minRight = minNodeValueInTree(root.right)
  if root.data <= maxLeft or root.data > minRight:
    return False

  leftSubTree = checkBST(root.left)
  rightSubTree = checkBST(root.right)

  return leftSubTree and rightSubTree



def checkBST2(root):
  
  # Base Case
  if root is None:
    return 100000, -100000, True
  
  leftMin, leftMax, leftBST = checkBST2(root.left)
  rightMin, rightMax, rightBST = checkBST2(root.right)

  maxValue = max(leftMax, rightMax, root.data)
  minValue = min(rightMin, leftMin, root.data)

  isBST = True
  if root.data <= leftMax or root.data > rightMax:
    isBST = False
  if not ( leftBST) or not( rightBST):
    isBST = False

  return minValue, maxValue, isBST



def checkBST3(root, min_range, max_range):
  if root is None:
    return True
  
  if (root.data < min_range or root.data > max_range):
    return False
  
  isLeftSubTree = checkBST3(root.left, min_range, root.data - 1)
  isRightSubTree = checkBST3(root.right, root.data, max_range)

  return isLeftSubTree and isRightSubTree







def maxNodeValueInTree(root):
  if root is None:
    return -100000
  
  leftSideMax = maxNodeValueInTree(root.left)
  rightSideMax = maxNodeValueInTree(root,right) 
  maxValue = max(root.data, leftSideMax, rightSideMax)
  return maxValue

def minNodeValueInTree(root):
  if root is None:
    return 100000
  
  leftSideMin = minNodeValueInTree(root.left)
  rightSideMin = minNodeValueInTree(root,right) 
  minValue = min(root.data, leftSideMin, rightSideMin)
  return minValue

  