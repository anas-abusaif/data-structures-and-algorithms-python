from collections import deque

class Vertex():
  def __init__(self,key):
    self.key = key
  
  def __str__(self):
    return str(self.key)

class Queue():
  def __init__(self):
    self.dq = deque()
  
  def enqueue(self,value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()
  
  def __len__ (self):
    return len(self.dq)

class Graph():
  def __init__(self):
    self._adjacency_list = {}
    
  def add_node(self,value):
    new_v = Vertex(value)
    new_v = str(new_v)
    self._adjacency_list[new_v] = []
    return new_v
    
  def add_edge(self,start_vertex,end_vertex,weight =0):
    if start_vertex not in self._adjacency_list:
      raise KeyError('Start vertex is not found in the graph')
    if end_vertex not in self._adjacency_list:
      raise KeyError('end vertex is not found in the graph') 
    self._adjacency_list[start_vertex].append((str(end_vertex),weight))  

  def get_nodes(self):
    return self._adjacency_list.keys()
    
  def neighbors(self,vertex):
    return self._adjacency_list[vertex]
  
  def size(self):
    return len(self._adjacency_list)


  def breath_first_search(self,start_vertex):
    output=[]
    queue = Queue()
    visited = set()
    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    while len(queue):
      current_vertex = queue.dequeue()
      output.append(current_vertex)
      for i in self._adjacency_list[current_vertex]:
        if i[0] not in visited:
          i=i[0]
          visited.add(i)
          queue.enqueue(i)
    return output


def business_trip(graph,cities:list):
    sum = 0
    flag = False
    for i in range(len(cities)-1):
        neighbors = graph._adjacency_list[cities[i]]
        print(neighbors)
        for neighbor in neighbors:
          if cities[i+1] == neighbor[0]:
            sum += neighbor[1]
            flag = True
            break
          else:
            sum += 0
            flag = False
    if not flag:
      return False,'$0'     
    return True,'$'+ str(sum)