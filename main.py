from Graph import Graph
from BaseNode import BaseNode
from pygame import mixer

import pygame, sys
from pygame.locals import *
import GameLogic

def main():
    pygame.init()
    # print(javierWaits)
    # print(timeToWait)
    mixer.init()
    mixer.music.load('./music/Faint.wav')
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    javierFinalList, AndreinaFinalList, javierWaits, timeToWait= GameLogic.startScreen()
    #ESTO ES PARA HACER LA INTERFAZ Y ACTUALIZAR LAS POSICIONES

main()
#     nodoPrimero= g.searchNODE(12,50)
#     if nodoPrimero is not None:
#         print(nodoPrimero.name)
# main()
