from Graph import Graph
from BaseNode import BaseNode
from pygame import mixer

import pygame, sys
from pygame.locals import *

def main():
    g = Graph()
    startNode = g.searchNODE(12,50)
    javierFinalList, AndreinaFinalList, javierWaits, timeToWait = g.findCouplePath(startNode)
    print(javierFinalList)
    print(AndreinaFinalList)
    # print(javierWaits)
    # print(timeToWait)

    #pruebas pygame
    pygame.init()
    mixer.init()
    mixer.music.load('./music/Faint.wav')
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)


    screen, javier, andreina, places, roads, backgrd = gui_init()

    javPos = [128, 128]
    andPos = [256, 384]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        for m in backgrd:
            screen.blit(m[0], (m[1], m[2]))

        for p in places:
            screen.blit(p[0], (p[1], p[2]))

        for r in roads:
            screen.blit(r[0], (r[1], r[2]))
        
        screen.blit(javier, (javPos[0], javPos[1]))
        screen.blit(andreina, (andPos[0], andPos[1]))
        pygame.display.update()
    
def gui_init():
    screen = pygame.display.set_mode((770, 700))
    screen.fill((0, 0, 0))

    javier = pygame.image.load('./sprites/javier1.png').convert()
    javier.set_colorkey((0, 0, 0))
    javier = pygame.transform.scale(javier, (64, 64))

    andreina = pygame.image.load('./sprites/andreina1.png').convert()
    andreina.set_colorkey((0, 0, 0))
    andreina = pygame.transform.scale(andreina, (64, 64))

    roadV = pygame.image.load('./sprites/subida.png').convert()
    roadV.set_colorkey((0, 0, 0))
    roadV = pygame.transform.scale(roadV, (64, 64))

    roadH = pygame.transform.rotate(roadV, 90)

    bRoad = pygame.image.load('./sprites/callerota.png').convert()
    bRoad.set_colorkey((0, 0, 0))
    bRoad = pygame.transform.scale(bRoad, (64, 64))

    cRoad = pygame.image.load('./sprites/fulldegente.png').convert()
    cRoad.set_colorkey((0, 0, 0))
    cRoad = pygame.transform.scale(cRoad, (64, 64))
    cRoad = pygame.transform.rotate(cRoad, 90)

    inter = pygame.image.load('./sprites/interseccion2.png').convert()
    inter.set_colorkey((0, 0, 0))
    inter = pygame.transform.scale(inter, (64, 64))

    javierHouse = pygame.image.load('./sprites/javiercasa.png').convert()
    javierHouse.set_colorkey((0, 0, 0))
    javierHouse = pygame.transform.scale(javierHouse, (64, 64))

    andreinaHouse = pygame.image.load('./sprites/andreinacasa.png').convert()
    andreinaHouse.set_colorkey((0, 0, 0))
    andreinaHouse = pygame.transform.scale(andreinaHouse, (64, 64))

    disco = pygame.image.load('./sprites/DARKNESS.png').convert()
    disco.set_colorkey((0, 0, 0))
    disco = pygame.transform.scale(disco, (64, 64))

    cerveceria = pygame.image.load('./sprites/barCERVECITA.png').convert()
    cerveceria.set_colorkey((0, 0, 0))
    cerveceria = pygame.transform.scale(cerveceria, (64, 64))

    bar = pygame.image.load('./sprites/PASIONBAR.png').convert()
    bar.set_colorkey((0, 0, 0))
    bar = pygame.transform.scale(bar, (64, 64))

    cafe = pygame.image.load('./sprites/local.png').convert()
    cafe.set_colorkey((0, 0, 0))
    cafe = pygame.transform.scale(cafe, (64, 64))

    background = pygame.image.load('./sprites/fondito.png').convert()
    background.set_colorkey((0, 0, 0))
    background = pygame.transform.scale(background, (64, 64))

    brokenCarreras = [12, 13, 14]
    commercialCalle = 51
    knownPlaces = [disco, bar, cerveceria,  cafe, javierHouse, andreinaHouse]
    knownPlacesNames = ['Cr14/Cll50', 'Cr11/Cll54', 'Cr12/Cll50', 'Cr10/Cll50', 'Cr14/Cll54', 'Cr13/Cll52']

    roads = []
    placesLocations = []
    backgrd=[]

    for cr in range(10, 16):
        for cll in range(50, 56):
            x = (15-cr) * 128

            y = (55-cll) * 128
            name = f'Cr{cr}/Cll{cll}'
            backgrd.append((background,x+64,y+64))
            if name in knownPlacesNames:
                block = knownPlaces[knownPlacesNames.index(f'Cr{cr}/Cll{cll}')]
                placesLocations.append((block, x+64, y-64))
            roads.append((inter, x, y))
            
            if cr not in brokenCarreras:
                roads.append((roadV, x, y+64))
            else:
                roads.append((bRoad, x, y+64))

            if cll != commercialCalle:
                roads.append((roadH, x+64, y))
            else:
                roads.append((cRoad, x+64, y))

    return screen, javier, andreina, placesLocations, roads, backgrd

main()
#     nodoPrimero= g.searchNODE(12,50)
#     if nodoPrimero is not None:
#         print(nodoPrimero.name)
# main()
