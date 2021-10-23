from Node import Node

class Stack():
  def __init__(self,top=None):
    self.top=top

  def push(self,value):
    node = Node(value)
    node.next_=self.top
    self.top=node


  def pop(self):
    try:
      popped=self.top
      self.top=self.top.next_
      popped.next_=None
      return popped
    except:
      raise Exception('this stack is empty')


  def peek(self):
    try:
      return self.top.data_
    except:
      raise Exception('this stack is empty')

  def is_empty(self):
    if self.top:
      return False
    else:
      return True