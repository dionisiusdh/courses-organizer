from graph import Graph, makeGraphFromTxt, getLowestDegree

g2 = makeGraphFromTxt("1")
g2.printGraph()
print(f"Lowest degree vertex: {getLowestDegree(g2)}")
