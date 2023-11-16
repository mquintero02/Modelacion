from Graph import Graph
from BaseNode import BaseNode
from pygame import mixer

import pygame, sys
from pygame.locals import *

def main():
    # print(javierWaits)
    # print(timeToWait)
    javierFinalList, AndreinaFinalList, javierWaits, timeToWait= startScreen()
    #ESTO ES PARA HACER LA INTERFAZ Y ACTUALIZAR LAS POSICIONES

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

def startScreen():
    g = Graph()

    pygame.init()
    screen, javier, andreina, places, roads, backgrd = gui_init()

    font = pygame.font.Font(None, 64)
    text = font.render('¡Bienvenido a la simulación!', True, (255, 255, 255))
    text_rect = text.get_rect(center=(380, 100))

    text2_font = pygame.font.Font(None, 44)
    text2 = text2_font.render('Indique la ruta de Javier y Andreina', True, (255, 255, 255))
    text_rect2 = text.get_rect(center=(415, 200))

    text3_font = pygame.font.Font(None, 32)
    text3 = text3_font.render('Café Sensación', True, (255, 255, 255))
    text_rect3 = text.get_rect(center=(800, 335))

    text4_font = pygame.font.Font(None, 32)
    text4 = text4_font.render('Bar Pasión', True, (255, 255, 255))
    text_rect4 = text.get_rect(center=(800, 435))

    text5_font = pygame.font.Font(None, 32)
    text5 = text5_font.render('Cerveceria Mi Rolita', True, (255, 255, 255))
    text_rect5 = text.get_rect(center=(800, 535))

    text6_font = pygame.font.Font(None, 32)
    text6 = text6_font.render('Nightclub The Darkness', True, (255, 255, 255))
    text_rect6 = text.get_rect(center=(800, 635))

    gray_rect = pygame.Rect(392, 292, 78, 78)
    gray_color = (185, 197, 194)
    gray_rect2 = pygame.Rect(392, 392, 78, 78)
    gray_rect3 = pygame.Rect(392, 492, 78, 78)
    gray_rect4 = pygame.Rect(392, 592, 78, 78)

    button = pygame.Rect(150, 300, 200, 60)
    pygame.draw.rect(screen, (0, 128, 255), button)

    button1 = pygame.Rect(150, 400, 200, 60)
    pygame.draw.rect(screen, (0, 128, 255), button1)

    button2 = pygame.Rect(150, 500, 200, 60)
    pygame.draw.rect(screen, (0, 128, 255), button2)

    button3 = pygame.Rect(150, 600, 200, 60)
    pygame.draw.rect(screen, (0, 128, 255), button3)


    button_text = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button = button_text.get_rect(center=button.center)
    button_text2 = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button2 = button_text2.get_rect(center=button1.center)
    button_text3 = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button3 = button_text3.get_rect(center=button2.center)
    button_text4 = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button4 = button_text4.get_rect(center=button3.center)

    pygame.draw.rect(screen, gray_color, gray_rect)
    pygame.draw.rect(screen, gray_color, gray_rect2)
    pygame.draw.rect(screen, gray_color, gray_rect3)
    pygame.draw.rect(screen, gray_color, gray_rect4)
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)
    screen.blit(text3, text_rect3)
    screen.blit(text4, text_rect4)
    screen.blit(text5, text_rect5)
    screen.blit(text6, text_rect6)
    screen.blit(button_text, text_rect_button)
    screen.blit(button_text2, text_rect_button2)
    screen.blit(button_text3, text_rect_button3)
    screen.blit(button_text4, text_rect_button4)
    screen.blit(places[0][0],(400,300))
    screen.blit(places[1][0],(400,400))
    screen.blit(places[2][0],(400,500))
    screen.blit(places[4][0],(400,600))

    pygame.display.flip()

    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    startNode = g.searchNODE(10,50)
                    javierFinalList, AndreinaFinalList, javierWaits, timeToWait = g.findCouplePath(startNode)
                    print(javierFinalList)
                    print(AndreinaFinalList)
                    return javierFinalList, AndreinaFinalList, javierWaits, timeToWait
                elif button1.collidepoint(mouse_pos):
                    startNode = g.searchNODE(11,54)
                    javierFinalList, AndreinaFinalList, javierWaits, timeToWait = g.findCouplePath(startNode)
                    print(javierFinalList)
                    print(AndreinaFinalList)
                    return javierFinalList, AndreinaFinalList, javierWaits, timeToWait
                elif button2.collidepoint(mouse_pos):
                    startNode = g.searchNODE(12,50)
                    javierFinalList, AndreinaFinalList, javierWaits, timeToWait = g.findCouplePath(startNode)
                    print(javierFinalList)
                    print(AndreinaFinalList)
                    return javierFinalList, AndreinaFinalList, javierWaits, timeToWait
                elif button3.collidepoint(mouse_pos):
                    startNode = g.searchNODE(14,50)
                    javierFinalList, AndreinaFinalList, javierWaits, timeToWait = g.findCouplePath(startNode)
                    print(javierFinalList)
                    print(AndreinaFinalList)
                    return javierFinalList, AndreinaFinalList, javierWaits, timeToWait
                waiting_for_click = False
        pygame.time.delay(10)
def gui_init():
    screen = pygame.display.set_mode((780, 700))
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
