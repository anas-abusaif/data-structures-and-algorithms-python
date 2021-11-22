from hash_table.hash_table import HashTable

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False
    
  def enqueue(self,item):
    self.data.append(item)
    
  def dequeue(self):
    return self.data.pop(0)

class BinaryTree: 
  
  def _init_(self):
    self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    breadth = Queue()
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items

def tree_intersection(tree1, tree2):
  try:
    content1 = tree1.bfs()
    content2 = tree2.bfs()
  except Exception:
    raise ValueError('please enter two valid binary trees')
  table = HashTable()
  for i in content1:
    table.add(str(i),str(i))

  intersection =[]
  for j in content2:
    if table.contains(str(j)):
      intersection +=[j]

  return intersection