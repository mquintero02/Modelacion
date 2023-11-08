from AdjNode import AdjNode
from BaseNode import BaseNode
from DMatrix import DMatrix

class Graph:

    def __init__(self):
        self.adjList = self.initGraph()
        self.times = {"javier": [5, 7, 10], "andreina": [7, 9, 12]} #Tiempos usados para dijkstra dependiendo de la persona
        self.startNodes = {"javier": "Casa de Javier", "andreina":"Casa de Andreina"}
        
      


    def dijkstra(self, tList, startNode, endNode):
        Dmatrix = DMatrix(self)
        Dmatrix.printDMatrix()
    
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
        self.dijkstra(self.times["javier"])

        # ruta minima andreina