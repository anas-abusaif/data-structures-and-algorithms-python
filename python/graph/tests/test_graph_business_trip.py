from graph.graph_business_trip import business_trip, Graph

def test_business_trip():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Metroville')
  v4 = graph.add_node('Monstropolis')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1,v2,150)
  graph.add_edge(v1,v3,82)
  graph.add_edge(v2,v3,99)
  graph.add_edge(v2,v4,42)
  graph.add_edge(v3,v4,105)
  graph.add_edge(v3,v5,37)
  graph.add_edge(v3,v6,26)
  graph.add_edge(v4,v6,73)
  graph.add_edge(v5,v6,250)
  cities_one_two_three = [v1,v2,v3]
  assert business_trip(graph,cities_one_two_three) == (True, '$249')