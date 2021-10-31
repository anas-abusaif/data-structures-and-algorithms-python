
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
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
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

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    function to in order the list using Trees
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order 

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)    

    walk(self.root)
    return list_of_items

  def tree_max(self):
    list_=self.post_order()
    return max(list_)

class Binary_search(BinaryTree):
  
  def __init__(self):
      super().__init__()
      self.root=None

  def add(self,value):
    node=Node(value)
    if self.root==None:
      self.root=node
      return
    
    current=self.root
    while current:
      if value > current.data:
        if current.right:
          current = current.right
        else:
          current.right = Node(value)
          return
      else:
        if current.left:
          current = current.left
        else:
           current.left = Node(value)
        return
  def contains(self,value):
    if not self.root:
      raise Exception("The Tree is Empty")

    else:
      temp = self.root
      while temp:
          if temp.data == value:
              return True
          elif temp.data > value:
              if not temp.left:
                  return False
              temp = temp.left
          else:
              if not temp.right:
                  return False
              temp = temp.right



tree=BinaryTree()

a_node = Node(1234)
b_node = Node(2)
c_node = Node(3)
d_node = Node(4)
a_node.left = b_node
a_node.right = c_node
b_node.left = d_node
tree.root=a_node 

print(tree.tree_max())