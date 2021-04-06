import ITB_MAP as fi
import Graph as graf
import fungsi as f
import aStar as algo

## Variabel Penampung Input
numNode = 0
listNode = []
listCoordinate = []
adjacencyMatrix = []

## Fungsi untuk validasi node
def isInNode(Node, listNodes):
	for i in range (len(listNodes)):
		if (listNodes[i]==Node):
			return True
	return False
	
## Pilih File Input
## Mungkin nanti bisa kita buat if buat pilihan petanya

## Inisiasi list dengan file input
numNode = fi.numNode
listNode = fi.listNodeITB
listCoordinate = fi.listKoordinatITB
adjacencyMatrix = fi.adjacencyMatrix


g = graf.Graph(numNode,listNode,listCoordinate,adjacencyMatrix)

start = input("Masukkan node start: ")
isIn=isInNode(start, listNode)
while(isInNode(start, listNode)==False):
	print("Node Tidak ditemukan silakan input ulang")
	start = input("Masukkan node tujuan: ")
	isIn=isInNode(start, listNode)
	
goal = input("Masukkan node tujuan: ")
isIn=isInNode(goal, listNode)
while(isIn==False):
	print("Node Tidak ditemukan silakan input ulang")
	goal = input("Masukkan node tujuan: ")
	isIn=isInNode(goal, listNode)
	
listIdxAnswer = algo.aStar(g,g.getIdxNode(start),g.getIdxNode(goal))
print(listIdxAnswer)
listNodeAnswer = g.convertIdxToNodeList(listIdxAnswer)
print(listNodeAnswer)
for node in listNodeAnswer:
    print(node)
