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

root = BTreeInput()
PrintBinaryTreeDetailed(root)
maxValue = Largest(root)
print(maxValue)