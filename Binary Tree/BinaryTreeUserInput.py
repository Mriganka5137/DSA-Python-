from BinaryTree import BinaryTree
from BinaryTree import PrintBinaryTreeDetailed


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

node = BTreeInput()
PrintBinaryTreeDetailed(node)