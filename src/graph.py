"""
Definisi kelas Graph dan method yang berhubungan dengan pemrosesan graph
"""

class Graph:
    def __init__ (self, vertices):
        self.E = dict()     # Edges / Kumpulan edge
        self.V = vertices   # Vertices / Kumpulan vertex

    # Menambahkan sebuah edge ke Graph
    def addEdge(self, e, v):
        if v == None: # Vertex tanpa derajat masuk
            self.E[e] = []
        else:
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

    # Cek apakah sebuah graph kosong
    # Graph kosong jika vertices dan edge kosong (0)
    def isGraphEmpty(self):
        return self.V == 0

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
        if (len(el) == 1): # Vertex tanpa derajat masuk
            graph.addEdge(el[0], None)
        else:
            for i in range(1, len(el)):
                graph.addEdge(el[0], el[i])

    return graph

# Mereturn vertex dengan derajat masuk terendah dari sebuah graph
def getLowestDegree(graph):
    d = {}

    # Mengambil value (derajat masuk) setiap vertex
    for k, v in graph.E.items():
        d[k] = len(v)

    # Mencari value (derajat masuk) terendah
    min_v = min(d.values())
    res = [k for k, v in d.items() if v==min_v]

    return res

# Menghapus semua hubungan edge pada graph p dari semua vertex ke vertex x
def removeAllEdgeFrom(graph, x):
    # Jika vertex k terhubung dengan x, hapus edge antara k dan x
    for k, v in graph.E.items():
        if x in v:
            v.remove(x)
 
    # Jika vertex tidak punya derajat masuk, maka hapus vertex
    if len(graph.E[x]) == 0:
        graph.E.pop(x)
        graph.V -= 1
    
