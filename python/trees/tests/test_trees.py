from trees import __version__
from trees.trees import BinaryTree
from trees.trees import Binary_search
from trees.trees import Node
from trees.breadth_first import breadth_first
from trees.tree_fizz_buzz import tree_fizz_buzz
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_bfs():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('A')
  b_node = Node('B')
  c_node = Node('C')
  d_node = Node('D')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  
  # set expected list
  expected = ["A", "B", "C", "D"]
  # set actual to return value of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs passed")

def test_bfs_2():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  
  # set expected list
  expected = ["1", "2", "3", "4"]
  # set actual to return value of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs_2 passed")



def test_pre_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  
  # set expected list
  expected = ["1", "2", "4", "3"]
  # set actual to return value of pre_order call
  actual = tree.pre_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_pre_order_ passed")

def test_post_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  
  # set expected list
  expected = ["4", "2", "3", "1"]
  # set actual to return value of post_order call
  actual = tree.post_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")  

def test_in_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  
  # set expected list
  expected = ["4", "2", "1", "3"]
  # set actual to return value of in_order call
  actual = tree.in_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_in_order_ passed")


def test_add_once():
     # Arrange
    # Create tree instance
    tree = Binary_search()
    # add "A" to the tree
    tree.add('A')
    # set expected list
    expected = "A"
    # set actual to the tree root value
    actual = tree.root.data
    # assert actual is same as expected
    assert actual == expected

def test_add_twice():
    # Arrange
    # Create tree instance
    tree = Binary_search()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    # set expected list
    expected = ["A","B"]
    # set actual to the tree root value
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected

def test_contains_value():
    # Arrange
    # Create tree instance
    tree = Binary_search()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = True
    # set actual to the tree root value
    actual = tree.contains("B")
    # assert actual is same as expected
    assert actual == expected

def test_not_contains_value():
   # Arrange
    # Create tree instance
    tree = Binary_search()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = False
    # set actual to the tree root value
    actual = tree.contains("E")
    # assert actual is same as expected
    assert actual == expected

def test_search_in_empty_tree():
   with pytest.raises(Exception):
       tree = Binary_search()
       actual = tree.contains("O")



def test_trees_max():
  # Arrange
  expected=1234
  # Act 
  tree=BinaryTree()
  a_node = Node(1234)
  b_node = Node(2)
  c_node = Node(3)
  d_node = Node(4)
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  tree.root=a_node 
  actual = tree.tree_max()
  # Assert
  assert actual==expected

def test_trees_max_empty():
   with pytest.raises(Exception):
       tree = Binary_search()
       actual = tree.tree_max()


def test_beadth_first():
  expected=[1234, 2, 3, 4, 1123, 950]
  tree=BinaryTree()
  a_node = Node(1234)
  b_node = Node(2)
  c_node = Node(3)
  d_node = Node(4)
  e_node=Node(1123)
  f_node=Node(950)
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  c_node.left=e_node
  e_node.left=f_node
  tree.root=a_node
  actual = breadth_first(tree)
  assert actual==expected


def test_tree_fizz_buzz():
  expected="1234"
  tree=BinaryTree()
  a_node = Node(1234)
  b_node = Node(2)
  c_node = Node(3)
  d_node = Node(5)
  e_node=Node(15)
  f_node=Node(30)
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  c_node.left=e_node
  e_node.left=f_node
  tree.root=a_node
  actual = tree_fizz_buzz(tree).root.data
  assert actual==expected