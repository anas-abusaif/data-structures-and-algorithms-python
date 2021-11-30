from graph.graph_depth_firat import Graph


def test_graph_depth_first():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Metroville')
  v4 = graph.add_node('Monstroplolis')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1, v2)
  graph.add_edge(v1, v4)
  graph.add_edge(v2,v1)
  graph.add_edge(v2,v3)
  graph.add_edge(v2,v4)
  graph.add_edge(v3,v2)
  graph.add_edge(v4,v1)
  graph.add_edge(v4,v2)
  graph.add_edge(v4,v5)
  graph.add_edge(v4,v6)
  graph.add_edge(v6,v4)
  graph.add_edge(v5,v4)
  assert graph.graph_depth_first(v1) == ["Pandora", "Arendelle", "Metroville", "Monstroplolis", "Narnia", "Naboo"]