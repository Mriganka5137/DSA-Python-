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

  