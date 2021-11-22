from hash_table.tree_intersection import tree_intersection, BinaryTree, Node
import pytest

def test_tree_intersection_error():
  with pytest.raises(ValueError):
    tree_intersection(2,3)


def test_tree_intersection():
  # Arrange
  expected = ['adham', 'ahmad', 'mohammad', 'murad', 'ashraf', 'anas']
  
  tree1=BinaryTree()
  a_node = Node('anas')
  b_node = Node('ahmad')
  c_node = Node('dario')
  d_node = Node('murad')
  e_node = Node('ashraf')
  f_node = Node('adham')
  g_node = Node('mohammad')
  h_node = Node('ali')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node
  c_node.left = e_node
  e_node.left = f_node
  f_node.right = g_node
  g_node.left = h_node
  tree1.root=a_node 

  tree2=BinaryTree()
  i_node = Node('firas')
  j_node = Node('adham')
  k_node = Node('mohammad')
  l_node = Node('ahmad')
  m_node = Node('anas')
  n_node = Node('ashraf')
  o_node = Node('murad')
  p_node = Node('yousef')
  i_node.left = j_node
  i_node.right = l_node
  l_node.left = k_node
  k_node.right=o_node
  o_node.left=p_node
  p_node.right=n_node
  n_node.right=m_node
  tree2.root=i_node 

  # Act
  actual = tree_intersection(tree1, tree2)

  # Assert
  assert actual == expected