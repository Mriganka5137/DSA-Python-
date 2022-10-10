from BinaryTree import BinaryTree
from BinaryTree import PrintBinaryTreeDetailed
from BinaryTreeUserInput import BTreeInput

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