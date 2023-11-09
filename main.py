from Graph import Graph
from BaseNode import BaseNode

def main():
    g = Graph()
    startNode = g.searchNODE(12,50)
    javierFinalList, AndreinaFinalList, javierWaits, timeToWait = g.findCouplePath(startNode)
    print(javierFinalList)
    print(AndreinaFinalList)
    print(javierWaits)
    print(timeToWait)
main()
#     nodoPrimero= g.searchNODE(12,50)
#     if nodoPrimero is not None:
#         print(nodoPrimero.name)
# main()
