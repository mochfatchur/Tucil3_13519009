import Graph as graf
import fungsi as f
import aStar as algo
import gmplot
import sys

# PATH untuk import data uji/test
sys.path.append('../test')

## ===================================== CATATAN ==============================================
## untuk mengganti file test, ubah "ITB_MAP" pada "import ITB_MAP as fi" menjadi file.py yang terdapat di Tucil3_13519009/test yaitu :
## AlunAlunBandung
## Buahbatu
## ITB_MAP
## PasarPermiri

## CONTOH
## awalnya "import ITB_MAP as fi" ingin diubah ke file test "AlunAlunBandung"
## maka menjadi "import AlunAlunBandung as fi"


import ITB_MAP as fi # ubah ini


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
	
## Inisiasi list dengan file input
numNode = fi.numNode
listNode = fi.listNode
listCoordinate = fi.listKoordinat
adjacencyMatrix = fi.adjacencyMatrix

## Inisialisasi graf
g = graf.Graph(numNode,listNode,listCoordinate,adjacencyMatrix)

## Menampilkan node-node dari graf
print("List of node dari peta yang dipilih: ")
for node in listNode:
        print('- ',node)
print()

## Meminta Input Pengguna
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

listNodeAnswer = g.convertIdxToNodeList(listIdxAnswer)
print()
print("Rute Terpendeknya adalah: ")
it = 0
for node in listNodeAnswer:
        if(it == 0):
                print("dari",node)
        else:
                print("ke",node)
        it+=1

for i in range(len(listIdxAnswer)-1):
        dist = f.euclideanDistance(listCoordinate[listIdxAnswer[i]],listCoordinate[listIdxAnswer[i+1]])
print()
print("Jarak terpendek dari " + start + " menuju " + goal + " adalah " + str(dist) + " meter.")


## Plotter

latitudeRute = g.convertIdxToCoordinateNodeX(listIdxAnswer)
longitudeRute = g.convertIdxToCoordinateNodeY(listIdxAnswer)

petaLatitude = fi.latitude
petaLongitude = fi.longitude

gmap = gmplot.GoogleMapPlotter(petaLatitude, petaLongitude, 18)
for i in range(numNode):
        for j in range(numNode):
                if(adjacencyMatrix[i][j] == 1):
                        latitude = [g.getNodeCoordinateX(i),g.getNodeCoordinateX(j)]
                        longitude = [g.getNodeCoordinateY(i),g.getNodeCoordinateY(j)]
                        gmap.scatter(latitude, longitude, '#ff0000', size = 5, marker = False)
                        gmap.plot(latitude, longitude, 'orange', edge_width = 1.5)

gmap.scatter(latitudeRute, longitudeRute, '#ff0000', size = 5, marker = False)
gmap.plot(latitudeRute, longitudeRute, 'blue', edge_width = 2.5)
gmap.draw("Visualisasi.html")
