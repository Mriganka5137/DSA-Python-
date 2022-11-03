class MapNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class Map:
  def __init__(self):
    self.bucketSize = 5
    self.bucket = []
    self.count = 0
    self.bucket = [None for i in range(self.bucketSize)]
  

  def size(self):
    return self.count

  
  def getIndex(self, hc):
    return (abs(hc) % (self.bucketSize))


  def rehash(self):
    
    temp = self.bucket
    self.bucket = [None for i in range(2 * self.bucketSize)]
    self.bucketSize = self.bucketSize * 2

    self.count = 0

    for head in temp:
      while head is not None:
        self.insert(head.key, head.value)
        head = head.next


  def insert(self, key, value):
    hc = hash(key)
    index = self.getIndex(hc)

    head = self.bucket[index]

    while(head is not None):
      if self.key == key:
        self.value = value
        return
      head = head.next

    head = self.bucket[index]
    newNode = MapNode(key, value)

    newNode.next = head
    self.bucket[index] = newNode
    self.count +=1

    loadFactor = self.count / self.bucketSize
    if loadFactor >= 0.7:
      self.rehash()
  


  def search(self, key):

    hc = hash(key)
    index = self.getIndex(hc)

    head = self.bucket[index]
    while(head is not None):
      if head.key == key:
        return head.value
      head = head.next
    
    return None


  def Remove(self, key):
    hc = hash(key)
    index = self.getIndex(hc)

    head = self.bucket[index]
    prev = None

    while head is not None:
      if head.key == key:
        if prev is None:
          self.bucket[index] = head.next
        else:
          prev.next = head.next
        self.count-= 1
        return head.value

      prev = head  
      head =  head.next
    return None


m = Map()
m.insert("Mriganka", 5137)
m.insert("Debashis", 5130)
print(m.size())
print(m.search("Mriganka"))    # Returns 5137
print(m.search("Debashis"))    # Returns 5130
print(m.search("Miganka"))     # Returns None as there is no such Key as MIGANKA

print(m.Remove("Debashis"))
print(m.size())

print(m.Remove("Debashis"))    # Returns None as DEBASHIS is being deleted above


