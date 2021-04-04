class Graph:

    __numOfNode = 0
    __node = []
    __adjacencyMatrix = []
    __listOfCoordinate = []
    
    def __init__(self, numOfNode, listOfNode, listOfCoordinate, adjaMatrix):
        self.__numOfNode = numOfNode
        self.__node = listOfNode
        self.__adjacencyMatrix = adjaMatrix
        self.__listOfCoordinate = listOfCoordinate
        
    def getNode(self, idxNode):
        return self.__node[idxNode]
    
    def getListOfNode(self):
        return self.__node

    def getAdjacencyMatrix(self):
        return self.__adjacencyMatrix
    
    def getListOfCoordinate(self):
        return self.__listOfCoordinate

    def getNodeCoordinate(self, nod):
        idxNode = self.getIdxNode(nod)
        return self.__listOfCoordinate[idxNode]
    
    def getNumOfNode(self):
        return self.__numOfNode
    
    def getIdxNode(self,nod):
        
        for i in range(self.__numOfNode):
            if(self.__node[i] == nod):
                return i
        return -1
    
    

