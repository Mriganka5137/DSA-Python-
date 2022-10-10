from BinaryTree import BinaryTree
from BinaryTree import PrintBinaryTreeDetailed
from BinaryTreeUserInput import BTreeInput

def SumOfNodes(root):
  if root == None:
    return 0
  leftCount = SumOfNodes(root.left)
  rightCount = SumOfNodes(root.right)
  return root.data + leftCount + rightCount

root = BTreeInput()
PrintBinaryTreeDetailed(root)
sum = SumOfNodes(root)
print(sum)