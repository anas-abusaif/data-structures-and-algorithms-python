# Graphs

A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.

## Challenge

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

* add node
  * Arguments: value
  * Returns: The added node
  * Add a node to the graph
* add edge
  * Arguments: 2 nodes to be connected by the edge, weight (optional)
  * Returns: nothing
  * Adds a new edge between two nodes in the graph
  * If specified, assign a weight to the edge
  * Both nodes should already be in the Graph
* get nodes
  * Arguments: none
  * Returns all of the nodes in the graph as a collection (set, list, or similar)
* get neighbors
  * Arguments: node
  * Returns a collection of edges connected to the given node
  * Include the weight of the connection in the returned collection
* size
  * Arguments: none
  * Returns the total number of nodes in the graph

## Approach & Efficiency

* add node
  * Time : O(1)
  * Space : O(1)
* add edge
  * Time : O(1)
  * Space : O(1)
* get neighbors
  * Time : O(1)
  * Space : O(1)
* size
  * Time : O(1)
  * Space : O(1)

## API

- [X] Node can be successfully added to the graph
- [X]An edge can be successfully added to the graph
- [X]A collection of all nodes can be properly retrieved from the graph
- [X]All appropriate neighbors can be retrieved from the graph
- [X]Neighbors are returned with the weight between nodes included
- [X]The proper size is returned, representing the number of nodes in the graph
- [X]A graph with only one node and edge can be properly returned
- [X]An empty graph properly returns null


Graph Breadth First
![whiteboard](Untitled.jpg)