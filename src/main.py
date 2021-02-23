from graph import Graph, makeGraphFromTxt

g = Graph(6)

g.addEdge(5, 2) 
g.addEdge(2, 6) 
g.addEdge(4, 1) 
g.addEdge(5, 1)

# g.printGraph()

g2 = makeGraphFromTxt("1")
g2.printGraph()
