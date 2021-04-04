import file_input as fi
import Graph as graf

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


## Test
g = graf.Graph(numNode,listNode,listCoordinate,adjacencyMatrix)

print(g.getNumOfNode())
print()
print(g.getAdjacencyMatrix())
print()
print(g.getListOfCoordinate())
print()
print(g.getListOfNode())
print()
print(g.getIdxNode("Labtek 5"))
print()
print(g.getNodeCoordinate("Labtek 5"))
