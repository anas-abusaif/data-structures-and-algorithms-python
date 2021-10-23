from stack_and_queue.Node import Node


class Queue():
  def __init__(self,front=None,back=None):
    self.front=front
    self.back=back


  def enqueue(self,value):
    node=Node(value)
    if self.front==None:
      self.front=node
    self.back.next_=node
    self.back=node


  def dequeue(self):
    try:
      dequeued=self.front
      self.front=self.front.next_
      return dequeued
    except:
      raise Exception('this queue is empty')
  

  def peek(self):
    try:
      return self.front.data_
    except:
      raise Exception('this queue is empty')

  
  def is_empty(self):
    if self.front:
      return False
    else:
      return True