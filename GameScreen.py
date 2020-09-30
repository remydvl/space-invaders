import pygame

pygame.font.init()

startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

gameText = startTextFont.render('game', False, (255, 255, 255))

# img de fond

backgroundImage = pygame.image.load("./assets/fond.png")

# img vaisseau
vaisseauImage = pygame.image.load("./assets/vaisseau.png")

vaisseauMoveToRight = False
vaisseauMoveToLeft = False

xVaisseau = 400

yVaisseau = 550

# img alien

alienImage = pygame.image.load("./assets/alien_1_0.png")

# img alien 2

alien2Image = pygame.image.load("./assets/alien_2_0.png")

# Ici on dessine l'ecran de jeu


def __draw(window, gameInfo):
    global xVaisseau

    global yVaisseau

    # Ici je centre la position en X des textes
    xText = window.get_width() / 2 - gameText.get_width() / 2

    window.blit(gameText, (xText, 200))

    window.blit(backgroundImage, (0, 0))

    window.blit(vaisseauImage, (xVaisseau, yVaisseau))

    compteur = 0

    while compteur < 16:
        alienSize = 32
        alienSpace = 60
        window.blit(alienImage, ((alienSize+alienSpace*compteur), 0))
        compteur = compteur+1

    compteur = 0

    while compteur < 16:
        alien2Size = 32
        alien2Space = 60
        alienySpace = 10
        window.blit(
            alien2Image, ((alien2Size+alien2Space*compteur), alienSize+alienySpace))
        compteur = compteur+1


# Ici on gere la mise à jour
def __update(window):
    marge=50
    global vaisseauMoveToRight, vaisseauMoveToLeft, xVaisseau
    if vaisseauMoveToRight:
        if xVaisseau < window.get_width()-32 - marge:
            xVaisseau = xVaisseau+10
    if vaisseauMoveToLeft:
        if xVaisseau > 0 + marge:
            xVaisseau = xVaisseau-10


# Ici on gere les evenements
def __events(gameInfo):
    global vaisseauMoveToRight, vaisseauMoveToLeft

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameInfo["done"] = True
        if event.type == pygame.KEYDOWN:
            # ici on suppose que vous avez fait un simple import pygame
            if event.key == pygame.K_RIGHT:
                # xVaisseau = xVaisseau+10
                vaisseauMoveToRight = True
            if event.key == pygame.K_LEFT:
                # xVaisseau = xVaisseau-10
                vaisseauMoveToLeft = True
        if event.type == pygame.KEYUP:
            # ici on suppose que vous avez fait un simple import pygame
            if event.key == pygame.K_RIGHT:
                vaisseauMoveToRight = False
            if event.key == pygame.K_LEFT:
                # xVaisseau = xVaisseau-10
                vaisseauMoveToLeft = False


def drawGameScreen(window, gameInfo):
    __events(gameInfo)
    __update(window)
    __draw(window, gameInfo)
