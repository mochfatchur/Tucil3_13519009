import fungsi as f

class Graph:
    # Atribut
    # __numOfNode
    # __node
    # __adjacencyMatrix
    # __listOfCoordinate
    # __weightedAdjacencyMatrix
    # __adjacencyList
    
    def __init__(self, numOfNode, listOfNode, listOfCoordinate, adjaMatrix):
        self.__numOfNode = numOfNode
        self.__node = listOfNode
        self.__adjacencyMatrix = adjaMatrix
        self.__listOfCoordinate = listOfCoordinate
        
        self.__weightedAdjacencyMatrix = [[0 for j in range(self.__numOfNode)] for i in range(self.__numOfNode)]
        for i in range(self.__numOfNode):
            for j in range(self.__numOfNode):
                if(self.__adjacencyMatrix[i][j] == 1):
                    p1 = self.__listOfCoordinate[i]
                    p2 = self.__listOfCoordinate[j]
                    weight = f.euclideanDistance(p1,p2) 
                    self.__weightedAdjacencyMatrix[i][j] = weight

        self.__adjacencyList = []
        for i in range(self.__numOfNode):
            neighbor = []
            for j in range(self.__numOfNode):
                if(self.__adjacencyMatrix[i][j] == 1):
                    neighbor = neighbor + [j]
            self.__adjacencyList = self.__adjacencyList + [neighbor]
            
        
        
    def getNode(self, idxNode):
        return self.__node[idxNode]
    
    def getListOfNode(self):
        return self.__node

    def getAdjacencyMatrix(self):
        return self.__adjacencyMatrix
    
    def getListOfCoordinate(self):
        return self.__listOfCoordinate

    def getNodeCoordinate(self, idxNode):
        return self.__listOfCoordinate[idxNode]

    def getNodeCoordinateX(self, idxNode):
        return self.getNodeCoordinate(idxNode)[0]
    
    def getNodeCoordinateY(self, idxNode):
        return self.getNodeCoordinate(idxNode)[1]
    
    def getWeightedAdjacencyMatrix(self):
        return self.__weightedAdjacencyMatrix

    def getAdjacencyList(self):
        return self.__adjacencyList

    def convertIdxToNodeList(self, listIdxNode):
        listNode = []
        for idx in listIdxNode:
            listNode = listNode + [self.getNode(idx)]
        return listNode

    def convertIdxToCoordinateNodeX(self, listIdxNode):
        listCoor = []
        for idx in listIdxNode:
            listCoor = listCoor + [self.getNodeCoordinate(idx)[0]]
        return listCoor

    def convertIdxToCoordinateNodeY(self, listIdxNode):
        listCoor = []
        for idx in listIdxNode:
            listCoor = listCoor + [self.getNodeCoordinate(idx)[1]]
        return listCoor

    def getNeighbors(self, idxV):
        return self.__adjacencyList[idxV]

    
    def getNumOfNode(self):
        return self.__numOfNode
    
    def getIdxNode(self,nod):
        
        for i in range(self.__numOfNode):
            if(self.__node[i] == nod):
                return i
        return -1
    
    

