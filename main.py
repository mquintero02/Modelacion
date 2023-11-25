from Graph import Graph
from BaseNode import BaseNode
from pygame import mixer

import pygame, sys, os
from pygame.locals import *

def main():
    x = 0
    y = 20
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    # print(javierWaits)
    # print(timeToWait)
    mixer.init()
    mixer.music.load('./music/Faint.wav')
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    javierFinalList, AndreinaFinalList, javierWaits, timeToWait= startScreen()
    #ESTO ES PARA HACER LA INTERFAZ Y ACTUALIZAR LAS POSICIONES

def startScreen():
    g = Graph()

    otherCalle = 50
    otherCarrera = 10

    print(otherCarrera)

    screen = pygame.display.set_mode((850, 850))
    screen.fill((0, 0, 0))

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

    background_surface = pygame.Surface(screen.get_size())
    background_surface.fill((38, 18, 79))
    screen.blit(background_surface, (0, 0))

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

    text7_font = pygame.font.Font(None, 32)
    text7 = text7_font.render('Otro lugar', True, (255, 255, 255))
    text_rect7 = text.get_rect(center=(350, 800))

    text8_font = pygame.font.Font(None, 32)
    text8 = text8_font.render('Carrera', True, (255, 255, 255))
    text_rect8 = text.get_rect(center=(600, 830))

    text9_font = pygame.font.Font(None, 32)
    text9 = text9_font.render('Calle', True, (255, 255, 255))
    text_rect9 = text.get_rect(center=(800, 830))

    text10_font = pygame.font.Font(None, 28)

    text11_font = pygame.font.Font(None, 32)
    text11 = text11_font.render(f'{otherCarrera}', True, (255, 255, 255))
    text_rect11 = text.get_rect(center=(630, 790))
    
    text12_font = pygame.font.Font(None, 32)
    text12 = text12_font.render(f'{otherCalle}', True, (255, 255, 255))
    text_rect12 = text.get_rect(center=(815, 790))


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

    button4 = pygame.Rect(380, 770, 30, 30)
    pygame.draw.rect(screen, (0, 255, 0), button4)

    button5 = pygame.Rect(270, 770, 30, 30)
    pygame.draw.rect(screen, (255, 0, 0), button5)

    button6 = pygame.Rect(560, 770, 30, 30)
    pygame.draw.rect(screen, (0, 255, 0), button6)

    button7 = pygame.Rect(460, 770, 30, 30)
    pygame.draw.rect(screen, (255, 0, 0), button7)

    button8 = pygame.Rect(670, 770, 100, 40)
    pygame.draw.rect(screen, (0, 128, 255), button8)


    button_text = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button = button_text.get_rect(center=button.center)
    button_text2 = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button2 = button_text2.get_rect(center=button1.center)
    button_text3 = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button3 = button_text3.get_rect(center=button2.center)
    button_text4 = text2_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button4 = button_text4.get_rect(center=button3.center)
    button_text5 = text2_font.render('+', True, (255, 255, 255))
    text_rect_button5 = button_text5.get_rect(center=button4.center)
    button_text6 = text2_font.render('-', True, (255, 255, 255))
    text_rect_button6 = button_text5.get_rect(center=button5.center)
    button_text7 = text2_font.render('+', True, (255, 255, 255))
    text_rect_button7 = button_text5.get_rect(center=button6.center)
    button_text8 = text2_font.render('-', True, (255, 255, 255))
    text_rect_button8 = button_text5.get_rect(center=button7.center)
    button_text9 = text10_font.render('Iniciar', True, (255, 255, 255))
    text_rect_button9 = button_text4.get_rect(center=button8.center)


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
    screen.blit(text7, text_rect7)
    screen.blit(text8, text_rect8)
    screen.blit(text9, text_rect9)
    screen.blit(text12, text_rect12)
    screen.blit(button_text, text_rect_button)
    screen.blit(button_text2, text_rect_button2)
    screen.blit(button_text3, text_rect_button3)
    screen.blit(button_text4, text_rect_button4)
    screen.blit(button_text5, text_rect_button5)
    screen.blit(button_text6, text_rect_button6)
    screen.blit(button_text7, text_rect_button7)
    screen.blit(button_text8, text_rect_button8)
    screen.blit(button_text9, text_rect_button9)
    screen.blit(cafe,(400,300))
    screen.blit(bar,(400,400))
    screen.blit(cerveceria,(400,500))
    screen.blit(disco,(400,600))

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
                    waiting_for_click = False
                elif button1.collidepoint(mouse_pos):
                    startNode = g.searchNODE(11,54)
                    waiting_for_click = False
                elif button2.collidepoint(mouse_pos):
                    startNode = g.searchNODE(12,50)
                    waiting_for_click = False
                elif button3.collidepoint(mouse_pos):
                    startNode = g.searchNODE(14,50)
                    waiting_for_click = False
                elif button4.collidepoint(mouse_pos):
                    if otherCarrera < 15:
                        otherCarrera += 1
                elif button5.collidepoint(mouse_pos):
                    if otherCarrera > 10:
                        otherCarrera -= 1
                elif button7.collidepoint(mouse_pos):
                    if otherCalle > 50:
                        otherCalle -= 1
                elif button6.collidepoint(mouse_pos):
                    if otherCalle < 55:
                        otherCalle += 1
                elif button8.collidepoint(mouse_pos):
                    if (otherCarrera == 14 and otherCalle == 54) or (otherCarrera == 13 and otherCalle == 52):
                        continue
                    else:
                        startNode = g.searchNODE(otherCarrera,otherCalle)
                        waiting_for_click = False


        pygame.draw.rect(screen, (38, 18, 79), pygame.Rect(325, 765, 40, 30))
        screen.blit(text11_font.render(f'{otherCarrera}', True, (255, 255, 255)), text_rect11)
        
        pygame.draw.rect(screen, (38, 18, 79), pygame.Rect(500, 765, 40, 30))
        screen.blit(text12_font.render(f'{otherCalle}', True, (255, 255, 255)), text_rect12)
        
        pygame.display.update()

        #pygame.time.delay(10)
    javierFinalList, AndreinaFinalList, javierWaits, timeToWait, javierPath, andreinaPath = g.findCouplePath(startNode)
    print(javierFinalList)
    print(AndreinaFinalList)
    simulation_screen(javierFinalList, AndreinaFinalList, javierWaits, timeToWait, javierPath, andreinaPath)

def simulation_screen(javierFinalList, AndreinaFinalList, javierWaits, timeToWait, javierPath, andreinaPath):
    screen, javier, andreina, places, roads, backgrd, javier2, javier3,andreina2,andreina3,secondStep= gui_init()

    javPos = [128, 128+100]
    andPos = [256, 384+100]

    newClock=pygame.time.Clock()

    clock = 0
    costoTotal = 0
    costoTotalAndreina = 0

    pathJavier = []
    pathAndreina = []

    javierCurrentPath = 0
    andreinaCurrentPath = 0

    javierStepsLeft = 0
    andreinaStepsLeft = 0

    javierVelocity = []
    andreinaVelocity = []

    javierMoving = False
    andreinaMoving = False

    if javierWaits:
        andreinaMoving = True
    else:
        javierMoving = True

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                        startScreen()
                        running = False

        for m in backgrd:
            screen.blit(m[0], (m[1], m[2]-28))

        for p in places:
            screen.blit(p[0], (p[1], p[2]+100))

        for r in roads:
            screen.blit(r[0], (r[1], r[2]-28))

        if clock == timeToWait:
            andreinaMoving = True
            javierMoving = True

        if javierMoving:
            if javierStepsLeft == 0:
                javierStepsLeft = javierFinalList[javierCurrentPath]['costo']
                javierVelocity = javierFinalList[javierCurrentPath]['direction']
                costoTotal += javierFinalList[javierCurrentPath]['costo']

            if javierVelocity[0] != 0:
                javPos[0] += 128/(javierVelocity[0]*javierFinalList[javierCurrentPath]['costo'])
                pathJavier.append(pygame.Rect(javPos[0]+10, javPos[1]+28, 32, 5))
            else:
                javPos[1] += 128/(javierVelocity[1]*javierFinalList[javierCurrentPath]['costo'])
                pathJavier.append(pygame.Rect(javPos[0]+30, javPos[1]+9, 5, 32))
            
            javierStepsLeft -= 1

            if javierStepsLeft == 0 and javierCurrentPath < len(javierFinalList)-1:
                javierCurrentPath += 1
            elif javierStepsLeft == 0 and javierCurrentPath == len(javierFinalList)-1:
                javierMoving = False

        if andreinaMoving:
            if andreinaStepsLeft == 0:
                andreinaStepsLeft = AndreinaFinalList[andreinaCurrentPath]['costo']
                andreinaVelocity = AndreinaFinalList[andreinaCurrentPath]['direction']
                costoTotalAndreina += AndreinaFinalList[andreinaCurrentPath]['costo']

            if andreinaVelocity[0] != 0:
                andPos[0] += 128/(andreinaVelocity[0]*AndreinaFinalList[andreinaCurrentPath]['costo'])
                pathAndreina.append(pygame.Rect(andPos[0]+17, andPos[1]+28, 32, 5))
            else:
                andPos[1] += 128/(andreinaVelocity[1]*AndreinaFinalList[andreinaCurrentPath]['costo'])
                pathAndreina.append(pygame.Rect(andPos[0]+30, andPos[1]+15, 5, 32))
            
            andreinaStepsLeft -= 1

            if andreinaStepsLeft == 0 and andreinaCurrentPath < len(AndreinaFinalList)-1:
                andreinaCurrentPath += 1
            elif andreinaStepsLeft == 0 and andreinaCurrentPath == len(AndreinaFinalList)-1:
                andreinaMoving = False

        for p in pathJavier:
            pygame.draw.rect(screen, (0, 128, 255), p)
        for p in pathAndreina:
            pygame.draw.rect(screen, (200, 0, 0), p)
        
        if javierMoving == True or andreinaMoving == True:
            if secondStep == True:
                screen.blit(javier, (javPos[0], javPos[1]))
            else:
                screen.blit(javier2, (javPos[0], javPos[1]))
        else:
            screen.blit(javier3, (javPos[0]+75, javPos[1]-35))
        if andreinaMoving == True or javierMoving == True:
            if secondStep == True:
                screen.blit(andreina2, (andPos[0], andPos[1]))
                secondStep=False
            else:
                screen.blit(andreina3, (andPos[0], andPos[1]))
                secondStep=True
        else:
            screen.blit(andreina, (andPos[0]+45, andPos[1]-40))
        pygame.display.update()
        clock += 1
        newClock.tick(10)

        button = pygame.Rect(1325, 360, 100, 60)
        pygame.draw.rect(screen, (0, 128, 255), button)

        text2_font = pygame.font.Font(None, 32)
        button_text = text2_font.render('menú', True, (255, 255, 255))
        text_rect_button = button_text.get_rect(center=button.center)
        screen.blit(button_text, text_rect_button)

        if javierMoving is False and andreinaMoving is False:
            pygame.draw.rect(screen, (0, 20, 20), pygame.Rect(900, 100, 340, 550))

            if javierWaits:
                textInterface2_font = pygame.font.Font(None, 40)
                textInterface2 = textInterface2_font.render(f'Javier debe esperar', True, (255, 255, 255))
                screen.blit(textInterface2, (930,150))
                

                textInterface4 = textInterface2_font.render(f'en su casita', True, (255, 255, 255))
                screen.blit(textInterface4, (980,200))
            else:
                textInterface3_font = pygame.font.Font(None, 40)
                textInterface3 = textInterface3_font.render(f'Andreina debe esperar', True, (255, 255, 255))
                screen.blit(textInterface3, (910,150))

                textInterface4 = textInterface3_font.render(f'en su casita', True, (255, 255, 255))
                screen.blit(textInterface4, (980,200))

            textInterface1_font = pygame.font.Font(None, 40)
            textInterface1 = textInterface1_font.render(f'Tiempo de espera:', True, (255, 255, 255))
            screen.blit(textInterface1, (945,300))

            textInterface1_font = pygame.font.Font(None, 40)
            textInterface1 = textInterface1_font.render(f'{timeToWait} minutos', True, (255, 255, 255))
            screen.blit(textInterface1, (995,350))

            textInterface1_font = pygame.font.Font(None, 40)
            textInterface1 = textInterface1_font.render('Tiempo de recorrido:', True, (255, 255, 255))
            screen.blit(textInterface1, (935,450))

            if javierWaits:
                textInterface1_font = pygame.font.Font(None, 40)
                textInterface1 = textInterface1_font.render(f'{costoTotalAndreina} minutos', True, (255, 255, 255))
                screen.blit(textInterface1, (995,500))
            else:
                textInterface1_font = pygame.font.Font(None, 40)
                textInterface1 = textInterface1_font.render(f'{costoTotal} minutos', True, (255, 255, 255))
                screen.blit(textInterface1, (995,500))

            pygame.draw.rect(screen, (40, 20, 26), pygame.Rect(930, 560, 560, 280))
            #ruta de javier
            textInterface1_font = pygame.font.Font(None, 40)
            textInterface1 = textInterface1_font.render('Ruta de Javier', True, (255, 255, 255))
            screen.blit(textInterface1, (1230,580))

           
            for i, place in enumerate(javierPath):
                textInterface1_font = pygame.font.Font(None, 25)
                textInterface1 = textInterface1_font.render(f'{i}) {place}', True, (255, 255, 255))
                screen.blit(textInterface1, (1260,620+(i*22)))
            #ruta de andreina
            textInterface1_font = pygame.font.Font(None, 40)
            textInterface1 = textInterface1_font.render('Ruta de Andreina', True, (255, 255, 255))
            screen.blit(textInterface1, (950,580))

           
            for i, place in enumerate(andreinaPath):
                textInterface1_font = pygame.font.Font(None, 25)
                textInterface1 = textInterface1_font.render(f'{i}) {place}', True, (255, 255, 255))
                screen.blit(textInterface1, (970,620+(i*22)))
                

           

         
     
            pygame.display.flip()

        else:
            image_path = './sprites/gato.png'
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (300, 200))

            pygame.draw.rect(screen, (0, 20, 20), pygame.Rect(900, 150, 340, 550))
            textInterface7_font = pygame.font.Font(None, 40)
            textInterface7 = textInterface7_font.render('CALCULANDO', True, (255, 255, 255))
            screen.blit(textInterface7, (975,200))

            textInterface7_font = pygame.font.Font(None, 40)
            textInterface7 = textInterface7_font.render('ESPERE', True, (255, 255, 255))
            screen.blit(textInterface7, (1010,550))

            screen.blit(image, (920, 300))
            pygame.display.flip()
        
        xy=15
        distance=18
        while xy != 9:
            textCrr = textInterface7_font.render(f'{xy}', True, (191, 255, 0))
            screen.blit(textCrr, (distance,815))
            distance+=128
            xy-=1
        textCrr = textInterface7_font.render(f'Carreras', True, (191, 255, 0))
        textCll = textInterface7_font.render(f'Calles', True, (233,189,21))
        screen.blit(textCrr, (distance-10,813))
        screen.blit(textCll, (780,30))

        yz=55
        distance2=119
        while yz != 49:
            textCrr = textInterface7_font.render(f'{yz}', True, (233,189,21))
            screen.blit(textCrr, (780,distance2))
            distance2+=128
            yz-=1


def gui_init():
    screen = pygame.display.set_mode((1550, 900))
    screen.fill((0, 0, 0))
    secondStep=True

    javier = pygame.image.load('./sprites/javier1.png').convert()
    javier.set_colorkey((0, 0, 0))
    javier = pygame.transform.scale(javier, (64, 64))
    

    javier2 = pygame.image.load('./sprites/javier2.png').convert()
    javier2.set_colorkey((0, 0, 0))
    javier2 = pygame.transform.scale(javier2, (64, 64))

    javier3 = pygame.image.load('./sprites/javier3.png').convert()
    javier3.set_colorkey((0, 0, 0))
    javier3 = pygame.transform.scale(javier3, (64, 64))

    andreina = pygame.image.load('./sprites/andreina1.png').convert()
    andreina.set_colorkey((0, 0, 0))
    andreina = pygame.transform.scale(andreina, (64, 64))

    andreina2 = pygame.image.load('./sprites/andreina2.png').convert()
    andreina2.set_colorkey((0, 0, 0))
    andreina2 = pygame.transform.scale(andreina2, (64, 64))

    andreina3 = pygame.image.load('./sprites/andreina3.png').convert()
    andreina3.set_colorkey((0, 0, 0))
    andreina3 = pygame.transform.scale(andreina3, (64, 64))

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
            roads.append((inter, x, y+128))
            
            if cr not in brokenCarreras:
                roads.append((roadV, x, y+64))
            else:
                roads.append((bRoad, x, y+64))

            if cll != commercialCalle:
                roads.append((roadH, x+64, y))
                roads.append((roadH, x+64, y+128))
            else:
                roads.append((cRoad, x+64, y+128))

    return screen, javier, andreina, placesLocations, roads, backgrd, javier2,javier3,andreina2,andreina3,secondStep

main()
#     nodoPrimero= g.searchNODE(12,50)
#     if nodoPrimero is not None:
#         print(nodoPrimero.name)
# main()
