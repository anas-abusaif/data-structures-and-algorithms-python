from typing import Hashable
from hash_table import HashTable

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

    

def tree_intersection(tree1, tree2 ):

  hashtable = HashTable()
  listtree1 = tree1.pre_order()
  for item in listtree1:
      hashtable.add(str(item),item)
  arr=[]
  listtree2 = tree2.pre_order()
  for element in listtree2:
      if hashtable.contains(str(element)):
          arr.append(element)
      else:
          hashtable.add(str(element), element)

  return arr


if __name__=='__main__':
  node1 = Node(150)
  node2 = Node(100)
  node3 = Node(250)
  node4 = Node(75)
  node5 = Node(160)
  node6 = Node(200)
  node7 = Node(350)
  node8 = Node(125)
  node9 = Node(175)
  node10 = Node(300)
  node11 = Node(500)
  node1.left=node2
  node1.right=node3
  node2.left=node4
  node2.right=node5
  node5.right=node9
  node5.left=node8
  node3.right=node7
  node3.left=node6
  node7.right=node11
  node7.left=node10
  tree1=BinaryTree()
  tree1.root=node1


  node12 = Node(42)
  node13 = Node(100)
  node14 = Node(600)
  node15 = Node(15)
  node16 = Node(160)
  node17 = Node(200)
  node18 = Node(350)
  node19 = Node(125)
  node20 = Node(175)
  node21 = Node(4)
  node22 = Node(500)
  node12.left=node13
  node12.right=node14
  node13.left=node15
  node13.right=node16
  node16.right=node20
  node16.left=node19
  node14.right=node18
  node14.left=node17
  node18.right=node22
  node18.left=node21
  tree2=BinaryTree()
  tree2.root=node12

print(tree_intersection(tree1,tree2))
