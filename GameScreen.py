import pygame

pygame.font.init()

startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

gameText = startTextFont.render('game', False, (255, 255, 255))

# img de fond

backgroundImage = pygame.image.load("./assets/fond.png")

# img vaisseau

vaisseauImage = pygame.image.load("./assets/vaisseau.png")

# img alien

alienImage = pygame.image.load("./assets/alien_1_0.png")

xVaisseau=400

yVaisseau=550

#img alien 2

alien2Image = pygame.image.load("./assets/alien_2_0.png")


def drawGameScreen(window, gameInfo):

    global xVaisseau

    global yVaisseau

    # Ici je centre la position en X des textes
    xText = window.get_width() / 2 - gameText.get_width() / 2

    window.blit(gameText, (xText, 200))

    window.blit(backgroundImage, (0 , 0))

    window.blit(vaisseauImage, (xVaisseau , yVaisseau))
    
    compteur=0
    
    while compteur < 16:
        alienSize=32
        alienSpace=60
        window.blit(alienImage, ((alienSize+alienSpace*compteur) , 0))
        compteur=compteur+1

    compteur=0

    while compteur < 16:
        alien2Size=32
        alien2Space=60
        alienySpace=10
        window.blit(alien2Image, ((alien2Size+alien2Space*compteur) , alienSize+alienySpace))
        compteur=compteur+1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameInfo["done"] = True
        if event.type == pygame.KEYDOWN:
            # ici on suppose que vous avez fait un simple import pygame
            if event.key == pygame.K_d:
                xVaisseau=xVaisseau+10
            if event.key == pygame.K_a:
                xVaisseau=xVaisseau-10

