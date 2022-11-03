class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0



    def printTreeHelper(self,root):
        if root == None:
            return
        print(root.data,end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data, end='')
        print()
        
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    

        
    def searchHelper(self, root, data):
        if root == None:
            return False
        if data > root.data:
            return self.searchHelper(root.right, data)
        if data < root.data:
            return self.searchHelper(root.left, data)
        if data == root.data:
            return True     
    
    
    def search(self, data):
        return self.searchHelper(self.root, data)
    
    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if root.data >= data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root    

        
    def insert(self, data):
        self.root = self.insertHelper(self.root, data)
        self.numNodes += 1
	
    

        
    
    def min(self,root):
      if root == None:
        return 10000
      if root.left == None:
        return root.data
      return self.min(root.left)

    def deleteHelper(self, root, data):
        if root == None:
            return False, None

        if data < root.data:
            deleted, root.left = self.deleteHelper(root.left, data)
            return deleted, root
        if data > root.data:
            deleted, root.right = self.deleteHelper(root.right, data)
            return deleted, root
        else:
            if root.left == None and root.right != None:
                return True, root.right
            elif root.right == None and root.left != None:
                return True, root.left
            elif root.right == None and root.right == None:
                return True, None
            else:
                replacement = self.min(root.right)
                root.data = replacement
                deleted, root.right = self.deleteHelper(root.right,replacement)
                return True, root  
    def delete(self, data):
        
        deleted, self.root = self.deleteHelper(self.root, data)
        if deleted:
          self.numNodes -= 1
        return deleted
    

   
        
        
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()