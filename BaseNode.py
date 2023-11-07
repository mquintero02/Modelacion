class BaseNode:
    
    def __init__(self, carrera, calle, name):
        self.adjacent = []
        self.carrera = carrera
        self.calle = calle
        self.name = name

    def insertAdj(self, adj):
        self.adjacent.append(adj)