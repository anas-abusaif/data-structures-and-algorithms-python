# from stack_and_queue.Node import Node
from Node import Node

class Stack():
  '''
  a class that instances a stack of nodes
  '''


  def __init__(self,top=None):
    self.top=top

  def push(self,value):
    '''
    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.
    '''
    
    node = Node(value)
    node.next_=self.top
    self.top=node


  def pop(self):
    '''
    Arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack
    Should raise exception when called on empty stack
    '''

    try:
      popped=self.top
      self.top=self.top.next_
      popped.next_=None
      return popped.data_
    except:
      raise Exception('this stack is empty')


  def peek(self):
    '''
    Arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack
    '''

    try:
      return self.top.data_
    except:
      raise Exception('this stack is empty')

  def is_empty(self):
    '''
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.
    '''

    if self.top:
      return False
    else:
      return True

