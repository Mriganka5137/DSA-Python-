from BinaryTree import BinaryTree
from BinaryTree import PrintBinaryTreeDetailed
from BinaryTreeUserInput import BTreeInput

def NoOfNodes(root):
  if root == None:
    return 0
  leftCount = NoOfNodes(root.left)
  rightCount = NoOfNodes(root.right)
  return 1 + leftCount + rightCount

root = BTreeInput()
PrintBinaryTreeDetailed(root)
print(NoOfNodes(root))
