
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
        
        listForGraphOrdered =[]
        finalList =[]
        for i in range(len(self.nodesIds)):
            firstString=  self.nodesIds[i]
            secondString=  self.predecesors[i]
            knownPlacesNames = ["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita",  "Café Sensación",
            "Casa de Javier", "Casa de Andreina"]
            knownPlaces = ['Cr14/Cll50', 'Cr11/Cll54', 'Cr12/Cll50', 'Cr10/Cll50', 'Cr14/Cll54', 'Cr13/Cll52']
            if firstString in knownPlacesNames:
                firstString = knownPlaces[knownPlacesNames.index(firstString)]
            if secondString in knownPlacesNames:
                secondString= knownPlaces[knownPlacesNames.index(secondString)]
            firstString=  firstString.split('/')
            if secondString is not None:
                secondString=  secondString.split('/')
                
            for firstPiece in firstString:
                if "Cr" in firstPiece:
                    firstCr= int(firstPiece.replace("Cr", ""))
                else:
                    firstCll=int(firstPiece.replace("Cll", ""))
            if secondString is not None:
                for secondPiece in secondString:
                    if "Cr" in secondPiece:
                        secondCr= int(secondPiece.replace("Cr", ""))
                    else:
                        secondCll=int(secondPiece.replace("Cll", ""))
                direction="none"
                if firstCr < secondCr:
                    direction="left"
                elif firstCr > secondCr:
                    direction="right"
                elif firstCll < secondCll:
                    direction="up"
                elif firstCll > secondCll:
                    direction="down"

            if  self.partOfPath[i] == True:
                print(f'Nodo: {self.nodesIds[i]} costoDesdeOrigen: {self.costFromOrigin[i]} Sucesor: {self.predecesors[i]}')
                dictionaryForGraphOrdered = {"NodoOrigen": self.nodesIds[i], "NodoDestino": self.predecesors[i], "costo":self.costFromOrigin[i], "direction":direction}
                listForGraphOrdered.append(dictionaryForGraphOrdered)
        listForGraphOrdered.sort(key=lambda x: x['costo'])
        for j in range(len(listForGraphOrdered)):
            newCostDude = listForGraphOrdered[j].get("costo")
            if listForGraphOrdered[j].get("costo") != 0:
                newCostDude = listForGraphOrdered[j].get("costo") - listForGraphOrdered[j-1].get("costo")
            dictionaryForFinalGraph = {"NodoOrigen": listForGraphOrdered[j].get("NodoOrigen"), "NodoDestino": listForGraphOrdered[j].get("NodoDestino"), "costo":newCostDude, "direction":listForGraphOrdered[j].get("direction")}
            if dictionaryForFinalGraph.get("NodoDestino") != None:
                finalList.append(dictionaryForFinalGraph)
        finalList.reverse()
        return finalList

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

   
        

