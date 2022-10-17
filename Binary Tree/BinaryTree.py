from HeightOfTree import height
import queue


class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

def PrintBinaryTree(root):
  if root is None:
    return
  print(root.data)
  PrintBinaryTree(root.left)
  PrintBinaryTree(root.right)

def PrintBinaryTreeDetailed(root):
  if root is None:
    return
  print(root.data,end=":")
  if root.left is not None:
    print("L:",root.left.data, end=",")
  if root.right is not None:
    print("R:",root.right.data, end="")
  print()
  PrintBinaryTreeDetailed(root.left)
  PrintBinaryTreeDetailed(root.right)

def BTreeInput():
  rootData = int(input())
  if rootData == -1:
    return None
  root = BinaryTree(rootData)
  left = BTreeInput()
  right = BTreeInput()
  root.left = left
  root.right = right
  return root


def Largest(root):
  if root is None:
    return -1
  leftSubTree = Largest(root.left)
  rightSubTree = Largest(root.right)
  largest = max(leftSubTree, rightSubTree, root.data)
  return largest

def LeafNode(root):
  if root is None:
    return 0
  if root.right is None and root.left is None:
    return 1
  leftTree = LeafNode(root.left)
  rightTree = LeafNode(root.right)
  return leftTree + rightTree


def PrintNodeAtDepthK(root, k):
  if root is None:
    return
  if k == 0:
    print(root.data)
    return
  PrintNodeAtDepthK(root.left, k-1)
  PrintNodeAtDepthK(root.right, k-1)
  return


def PrintNodeAtDepthKV2(root, k, d=0):
  if root is None:
    return
  if d == k:
    print(root.data,end=' ')
  PrintNodeAtDepthKV2(root.left,k,d+1)
  PrintNodeAtDepthKV2(root.right,k,d+1)
  return

def changeToDepthTree(root, d=0) :
  if root is None:
    return
  root.data = d
  changeToDepthTree(root.left, d+1)
  changeToDepthTree(root.right, d+1)
  return

def isNodePresent(root, x):
    # Write your code here.
    if root is None:
        return False
    elif root.data == x:
        return True
    else:
        return isNodePresent(root.left, x) or isNodePresent(root.right,x)
  
def RemoveLeaves(root):
  if root == None:
    return None
  if root.left == None and root.right == None:
    return None
  root.left = RemoveLeaves(root.left)
  root.right = RemoveLeaves(root.right)
  return root

def Height(root):
  if root is None:
    return 0
  return 1 + max(Height(root.left), Height(root.right))

def CheckBalancedTree(root):
  if root is None:
    return
  leftHeight = Height(root.left)
  rightHeight = Height(root.right)
  if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1:
    return False
  left = CheckBalancedTree(root.left)
  right = CheckBalancedTree(root.right)
  if left and right:
    return True
  else:
    return False


def checkHeightAndIsBalanced(root):
  if root == None:
    return 0, True
  lh, isLeftBalanced = checkHeightAndIsBalanced(root.left)
  rh, isRightBalanced = checkHeightAndIsBalanced(root.right)

  h = 1 + max(lh, rh)
  if (rh - lh) > 1 or (lh -rh) > 1:
    return h, False
  
  if isLeftBalanced and isRightBalanced:
    return h, True
  else:
    return h, False


def BinaryTreeLevelWiseInput():
  q =queue.Queue()
  print("Enter Root Node")
  rootNode = (int)(input())
  if rootNode == -1:
    return None
  root = BinaryTree(rootNode)
  q.put(root)
  while(not q.empty()):
    node = q.get()
    print("Enter leftChild data for ",node.data)
    leftChildData = int(input())
    if leftChildData != -1:
      leftChild = BinaryTree(leftChildData)
      node.left = leftChild
      q.put(leftChild)

    print("Enter Right Child data for ",node.data)
    rightChildData = int(input())
    if rightChildData != -1:
      rightChild = BinaryTree(rightChildData)
      node.right = rightChild
      q.put(rightChild)
  return root
  


root = BinaryTreeLevelWiseInput()
# root = BTreeInput()
# maxValue = Largest(root)
# print(maxValue)
# print(LeafNode(root))
# PrintNodeAtDepthKV2(root, 2, 0)
# changeToDepthTree(root, d=0)
# root = RemoveLeaves(root)
# height,isBalanced = checkHeightAndIsBalanced(root)
# PrintBinaryTreeDetailed(root)
# print(height,isBalanced)
PrintBinaryTreeDetailed(root)