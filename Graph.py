from AdjNode import AdjNode
from BaseNode import BaseNode
from DMatrix import DMatrix

class Graph:

    def __init__(self):
        self.adjList = self.initGraph()
        self.times = {"javier": [5, 7, 10], "andreina": [7, 9, 12]} #Tiempos usados para dijkstra dependiendo de la persona
        self.startNodes = {"javier": self.searchNODE(14,54), "andreina":self.searchNODE(13,52)}
    
    
    #inicializar el grafo como lista de adyacencia, guardandola en adjList
    def initGraph(self):
        nodes = []

        brokenCarreras = [12, 13, 14]
        commercialCalle = 51
        knownPlacesNames = ["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita",  "Café Sensación", 
                      "Casa de Javier", "Casa de Andreina"]
        knownPlaces = ['Cr14/Cll50', 'Cr11/Cll54', 'Cr12/Cll50', 'Cr10/Cll50', 'Cr14/Cll54', 'Cr13/Cll52']

        for cr in range(10, 16):
            for cll in range(50, 56):

                name = f'Cr{cr}/Cll{cll}'

                if name in knownPlaces:
                    name = knownPlacesNames[knownPlaces.index(f'Cr{cr}/Cll{cll}')]

                bn = BaseNode(cr, cll, name)

                adjByCr = [cr-1, cr+1]
                adjByCll = [cll-1, cll+1]

                changeCrTime = 0
                changeCllTime = 0

                if cll == commercialCalle:
                    changeCrTime = 2
                
                if cr in brokenCarreras:
                    changeCllTime = 1

                for adj in adjByCr:
                    if adj >=10 and adj <= 15:
                        bn.insertAdj(AdjNode(changeCrTime, adj, cll))

                for adj in adjByCll:
                    if adj >= 50 and adj <= 55:
                        bn.insertAdj(AdjNode(changeCllTime, cr, adj))

                nodes.append(bn)
        return nodes
                
    def printGraphInConsole(self):
        for node in self.adjList:
            print(node.name)
            for a in node.adjacent:
                print(f'{a.carrera}/{a.calle}: {a.crossTime}')

    def findCouplePath(self, endNode):
        javierStart = self.startNodes["javier"]
        andreinaStart = self.startNodes["andreina"]

        # ruta minima javier
        resultMatrixJ = self.dijkstra(self.times["javier"], javierStart, endNode)
        resultMatrixJ.printDMatrix()
        # ruta minima andreina
        resultMatrixA = self.dijkstra(self.times["andreina"], andreinaStart, endNode)

    def dijkstra(self, tList, startNode, endNode):
        currentNode = startNode
        Dmatrix = DMatrix(self, startNode)
        while Dmatrix.nodesUnvisitedExist():
            #ubico indicce de nodo actual
            currentNodeIndex = self.searchNodeIndex(currentNode.carrera, currentNode.calle)
            #actualizo los costos de los nodos adyacentes
            nodesToUpdate = self.adjList[currentNodeIndex].adjacent
            for node in nodesToUpdate:
                index = self.searchNodeIndex(node.carrera, node.calle)
                newCost = Dmatrix.costFromOrigin[currentNodeIndex]+tList[node.crossTime]
                # si el nodo fue visiado y su nuevo camino es menos costoso que el existente, actualizalo
                if (not Dmatrix.visitedList[index]) and (newCost < Dmatrix.costFromOrigin[index]):
                    Dmatrix.costFromOrigin[index] = newCost
                    Dmatrix.predecesors[index] = currentNode.name
            #Marco como visitado el nodo actual
            Dmatrix.visitedList[currentNodeIndex] = True
            #Seteo el siguiente nodo a revisar como current Node
            currentNode = self.adjList[self.chooseNodeToCheck(Dmatrix)]
        return Dmatrix
           
           
            

            
        # Dmatrix.printDMatrix()
    # retorna indice del proximo nodo a chequear
    def chooseNodeToCheck(self, Dmatrix):
        currentLowest = 1000
        currentLowestIndex = 0
        for i in range(len(Dmatrix.nodesIds)):
            # index = self.searchNodeIndex(node.carrera, node.calle)
            if (not Dmatrix.visitedList[i]) and (Dmatrix.costFromOrigin[i] < currentLowest):
                currentLowest = Dmatrix.costFromOrigin[i]
                currentLowestIndex = i
        return currentLowestIndex



    def searchNODE(self,cr,cll):
        notAvailable = False
        knownPlacesNames = ["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita",  "Café Sensación",
        "Casa de Javier", "Casa de Andreina"]
        knownPlaces = ['Cr14/Cll50', 'Cr11/Cll54', 'Cr12/Cll50', 'Cr10/Cll50', 'Cr14/Cll54', 'Cr13/Cll52']
        name = f'Cr{cr}/Cll{cll}'
        if name in knownPlaces:
            name = knownPlacesNames[knownPlaces.index(f'Cr{cr}/Cll{cll}')]

        for node in self.adjList:
            if node.name == name:
                return node
            else:
                notAvailable = True
        if notAvailable is True:
            return None
        
    def searchNodeIndex(self,cr,cll):
        notAvailable = False
        knownPlacesNames = ["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita",  "Café Sensación",
        "Casa de Javier", "Casa de Andreina"]
        knownPlaces = ['Cr14/Cll50', 'Cr11/Cll54', 'Cr12/Cll50', 'Cr10/Cll50', 'Cr14/Cll54', 'Cr13/Cll52']
        name = f'Cr{cr}/Cll{cll}'
        if name in knownPlaces:
            
            name = knownPlacesNames[knownPlaces.index(f'Cr{cr}/Cll{cll}')]

        for index, node in enumerate(self.adjList):
            if node.name == name:
                return index
            else:
                notAvailable = True
        if notAvailable is True:
            return None
    
    
