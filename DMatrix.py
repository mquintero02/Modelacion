
class DMatrix:
        
    def __init__(self, Graph):
        self.nodesIds = []
        self.visitedList = []
        self.costFromOrigin = []
        self.predecesors = []
        self.timeStamps = []
        self.fillArrays(Graph)

    def fillArrays(self, Graph):
        for node in Graph.adjList:
            self.nodesIds.append(node.name)
            self.visitedList.append(False)
            self.costFromOrigin.append(999)
            self.predecesors.append("")
            self.timeStamps.append(None)

    def printDMatrix(self):
        for node in self.nodesIds:
            print(node)

