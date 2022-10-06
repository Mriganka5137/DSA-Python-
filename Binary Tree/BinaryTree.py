class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

bnt1 = BinaryTree(1)
bnt2 = BinaryTree(2)
bnt3 = BinaryTree(3)
bnt1.left = bnt2
bnt1.right = bnt3