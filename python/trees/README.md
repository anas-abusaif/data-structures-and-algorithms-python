# Trees
A tree data structure is a non-linear data structure because it does not store in a sequential manner. It is a hierarchical structure as elements in a Tree are arranged in multiple levels. In the Tree data structure, the topmost node is known as a root node. Each node contains some data, and data can be of any type.
## Challenge
Create a Binary Search Tree class

This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

Add

Arguments: value

Return: nothing

Adds a new node with that value in the correct location in the binary search tree.

Contains

Argument: value

Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
Big O of time = O(n^2)
Big O of space = O(1)
## API
[x] - Can successfully instantiate an empty tree
[x] - Can successfully instantiate a tree with a single root node
[x] - Can successfully add a left child and right child to a single root node
[x] - Can successfully return a collection from a preorder traversal
[x] - Can successfully return a collection from an inorder traversal
[x] - Can successfully return a collection from a postorder traversal