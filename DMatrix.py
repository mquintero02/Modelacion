
class DMatrix:
        
    def __init__(self, Graph, startNode):
        self.nodesIds = []
        self.visitedList = []
        self.costFromOrigin = []
        self.predecesors = []
        self.timeStamps = []
        self.partOfPath = []
        self.fillArrays(Graph, startNode)

    def fillArrays(self, Graph, startNode):
        for node in Graph.adjList:
            self.nodesIds.append(node.name)
            if node.name == startNode.name:
                self.visitedList.append(True)
                self.costFromOrigin.append(0)
            else:
                self.visitedList.append(False)
                self.costFromOrigin.append(999)
            
            self.partOfPath.append(False)
            self.predecesors.append(None)
            self.timeStamps.append(None)

    def printDMatrix(self):
        for i in range(len(self.nodesIds)):
            print(f'Nodo: {self.nodesIds[i]} visitado: {self.visitedList[i]} costoDesdeOrigen: {self.costFromOrigin[i]} predecesor: {self.predecesors[i]}, esCamino: {self.partOfPath[i]}')
    def printBasic(self):
        for i in range(len(self.nodesIds)):
            print(f'Nodo: {self.nodesIds[i]} costoDesdeOrigen: {self.costFromOrigin[i]} predecesor: {self.predecesors[i]}')


    def nodesUnvisitedExist(self):
        nodeUnvisitedExist = False
        for boolean in self.visitedList:
            if boolean == False:
                nodeUnvisitedExist = True
                return nodeUnvisitedExist
        return nodeUnvisitedExist
    
    def identifyPath(self, startNode, endNode, graph):
        currentNode = startNode
        while currentNode != endNode:
            currentIndex = graph.searchNodeIndex(currentNode.carrera, currentNode.calle)
            self.partOfPath[currentIndex] = True
            currentNode = graph.searchNodeByName(self.predecesors[currentIndex])
        currentIndex = graph.searchNodeIndex(endNode.carrera, endNode.calle)
        self.partOfPath[currentIndex] = True

   
        

