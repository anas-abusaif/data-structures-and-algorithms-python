from stack_and_queue.Node import Node

class Queue():
  '''
  a class that istances a queue of Nodes
  '''
  def __init__(self,front=None,back=None):
    self.front=front
    self.back=back


  def enqueue(self,value):
    '''
    Arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.

    '''

    node=Node(value)
    if self.front==None:
      self.front=node
      self.back=node
    else:
      self.back.next_=node
      self.back=node
    

  def dequeue(self):
    '''
    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue
    '''

    try:
      dequeued=self.front
      self.front=dequeued.next_
      dequeued.next_=None
      return dequeued.data_
    except:
      raise Exception('this queue is empty')

  

  def peek(self):
    '''
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack

    '''

    try:
      return self.front.data_
    except:
      raise Exception('this queue is empty')

  
  def is_empty(self):
    '''
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty
    '''

    if self.back:
      return False
    else:
      return True
