from Graph import Graph
from BaseNode import BaseNode

def main():
    g = Graph()
    
    startNode = g.searchNODE(11,54)
    g.findCouplePath(startNode)

main()
#     nodoPrimero= g.searchNODE(12,50)
#     if nodoPrimero is not None:
#         print(nodoPrimero.name)
# main()
