import queue
class GenericTree:
  def __init__(self, data):
    self.data = data
    self.children = list()


  def PrintTree(self, root):
    if root is None:
      return
    
    print(root.data, end=',')

    for child in root.children:
      self.PrintTree(child)
  

def PrintTreeDetailed(root):
  if root is None:
    return
  
  print(root.data, ':', end='')

  for child in root.children:
    print(child.data,end=',')
  
  print()

  for child in root.children:
    PrintTreeDetailed(child)


def takeTreeInput():
  print("Enter the root")

  rootdata = int(input())
  if rootdata == -1:
    return None
  
  root = GenericTree(rootdata)

  print("Enter the number of children for ", rootdata)
  noOfChildren = int(input())

  for i in range(noOfChildren):
    child = takeTreeInput()
    root.children.append(child)
  return root


def noOfNodes(root):
  if root is None:
    return 0
  
  count = 1

  for child in root.children:
    count += noOfNodes(child)
  
  return count


def height(root):
  if not root:
    return 0
  
  maxHeight = 0
  
  for child in root.children:
    childHeight = height(child)
    maxHeight = max(maxHeight, childHeight)
  return 1 + maxHeight


def takeInputLevelWise():
  q = queue.Queue()
  print("enter the root node")
  
  rootNode = int(input())
  if rootNode == -1:
    return None
  
  root = GenericTree(rootNode)
  q.put(root)
  
  while(not(q.empty())):
    curr_node = q.get()
    print("enter the no of children for ",curr_node.data)
    noOfChild = int(input())

    for i in range(noOfChild):
      print("enter child for root ", curr_node.data)
      childData = int(input())
      childNode = GenericTree(childData)
      curr_node.children.append(childNode)
      q.put(childNode)
  
  return root




node = takeInputLevelWise()
PrintTreeDetailed(node)
print(noOfNodes(node))
print(height(node))




# n1 = GenericTree(1)
# n2 = GenericTree(2)
# n3 = GenericTree(3)
# n4 = GenericTree(4)
# n5 = GenericTree(5)

# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n2.children.append(n5)


