from Graph import Graph
from BaseNode import BaseNode

def main():
    g = Graph()
    nodoPrimero= g.searchNODE(11,52)
    if nodoPrimero is not None:
        print(nodoPrimero.name)
main()
