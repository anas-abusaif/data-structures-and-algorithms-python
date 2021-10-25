from stack_and_queue.Node import Node

class dog:
  def __init__(self):
    self.type='dog'


class cat:
  def __init__(self):
    self.type='cat'



class AnimalShelter:
  def __init__(self):
   self.front=None
   self .back=None
  
  def enqueue(self,animal):
    node=Node()
    node.data_=animal
    if self.front==None:
      self.front=node
      self.back=node
    else:
      self.back.next_=node
      self.back=node
  

  def dequeue(self,pref):
    if pref != 'cat' or pref != 'dog':
      return 'NULL'
    temp=self.front
    prev=self.front
    while True:
      if temp.data_.type == pref:
        out=temp
        if out ==self.front:
          self.front=self.front.next_
        prev.next_=temp.next_
        return out
        break
      elif temp.data_.type != pref:
        prev=temp
        temp=self.front.next_
        



