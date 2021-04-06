import file_input as fi
import Graph as graf
import fungsi as f
import aStar as algo

## Variabel Penampung Input
numNode = 0
listNode = []
listCoordinate = []
adjacencyMatrix = []

## Pilih File Input
## Mungkin nanti bisa kita buat if buat pilihan petanya

## Inisiasi list dengan file input
numNode = fi.numNode
listNode = fi.listNodeITB
listCoordinate = fi.listKoordinatITB
adjacencyMatrix = fi.adjacencyMatrix


g = graf.Graph(numNode,listNode,listCoordinate,adjacencyMatrix)

start = input("Masukkan node start: ")
goal = input("Masukkan node tujuan: ")

listIdxAnswer = algo.aStar(g,g.getIdxNode(start),g.getIdxNode(goal))
print(listIdxAnswer)
listNodeAnswer = g.convertIdxToNodeList(listIdxAnswer)
print(listNodeAnswer)
for node in listNodeAnswer:
    print(node)
