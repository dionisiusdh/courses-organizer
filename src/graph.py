import string

"""
Definisi kelas Graph
"""
from collections import defaultdict

class Graph:
    def __init__ (self, vertices):
        self.E = dict() # Edges
        self.V = vertices   # Vertices

    # Menambahkan sebuah edge ke Graph
    def addEdge(self, e, v):
        if e not in self.E.keys():
            self.E[e] = [v]
        else:
            self.E[e].append(v)

    # Mengoutput struktur graph dengan format contoh:
    # A -> B -> C
    # D
    # E -> F
    def printGraph(self):
        for k, v in self.E.items():
            print(str(k) + " ", end="")
            for v_item in v:
                print("->", end="")
                print(f" {v_item} ", end="")
            print()

# Membaca data graph dari file .txt dan mereturn sebuah Graph
# Path default : "./test" 
# file_name tanpa dituliskan ekstensi (.txt)
def makeGraphFromTxt(file_name):
    # Variabel
    res = []
    res_cleaned = []
    all_vertex = list()
    
    # Open dan read file
    f = open(f"./test/{file_name}.txt", "r")

    # Append setiap line ke array result
    for line in f:
        res.append(line.split(","))

    # Cleaning tanda ' ', '.' dan '/n'
    for el in res:
        res_cleaned.append([])
        for i in range(len(el)):
            el_cleaned = el[i].replace(" ", "").replace(".", "").replace("\n", "")
            res_cleaned[len(res_cleaned)-1].append(el_cleaned)
    
    # Menyimpan semua vertex yang ada
    for el in res_cleaned:
        for v in el:
            all_vertex.append(v)

    all_vertex = set(all_vertex)

    # Membuat sebuah graph dengan vertex sebanyak panjang himpunan all_vertex
    graph = Graph(len(all_vertex))

    # Adding setiap edge yang ada
    for el in res_cleaned:
        for i in range(1, len(el)):
            graph.addEdge(el[0], el[i])

    return graph