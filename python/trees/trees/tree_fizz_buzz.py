from trees.trees import BinaryTree
from trees.trees import Node


def tree_fizz_buzz(tree):
  new_tree=BinaryTree
  def assign_nodes(node):
    node_fizz_buzz=None

    if node.data % 15 == 0 :
      node_fizz_buzz='FizzBuzz'

    elif node.data % 3 == 0 :
      node_fizz_buzz='Fizz'

    elif node.data % 5 == 0 :
        node_fizz_buzz='Buzz'

    else:
      node_fizz_buzz=str(node.data)

    new_node=Node(node_fizz_buzz)

    if node.left:
      new_node.left=assign_nodes(node.left)
    
    if node.right:
      new_node.right=assign_nodes(node.right)
    
    return new_node

  original_root=tree.root
  new_tree.root=assign_nodes(original_root)
  return new_tree


