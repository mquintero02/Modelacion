from Graph import Graph
from BaseNode import BaseNode

def main():
    g = Graph()
    
    endNode = g.searchNODE(10,50)
    g.findCouplePath(endNode)

main()
#     nodoPrimero= g.searchNODE(12,50)
#     if nodoPrimero is not None:
#         print(nodoPrimero.name)
# main()
