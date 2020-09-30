import pygame

pygame.font.init()

startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

gameText = startTextFont.render('game', False, (255, 255, 255))

# img de fond

backgroundImage = pygame.image.load("./assets/fond.png")

# projectil

projectil = {
    "image": pygame.image.load("./assets/shoot.png"),
    "x": 0,
    "y": 0,
    "destroyed": False
}

# vaisseau

vaisseau = {
    "image": pygame.image.load("./assets/vaisseau.png"),
    "moveToRight": False,
    "moveToLeft": False,
    "x": 400,
    "y": 550,
    "projectilsList": []
}

# img alien

alienImage = pygame.image.load("./assets/alien_1_0.png")

# img alien 2

alien2Image = pygame.image.load("./assets/alien_2_0.png")


def __draw(window, gameInfo):
    # Ici on dessine l'ecran de jeu
    # Ici je centre la position en X des textes
    xText = window.get_width() / 2 - gameText.get_width() / 2

    window.blit(gameText, (xText, 200))

    window.blit(backgroundImage, (0, 0))

    window.blit(vaisseau["image"], (vaisseau["x"], vaisseau["y"]))

    for bullet in vaisseau["projectilsList"]:
        window.blit(bullet["image"], (bullet["x"], bullet["y"]))

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
            alien2Image,
            ((alien2Size+alien2Space*compteur), alienSize+alienySpace)
        )
        compteur = compteur+1


def __update(window):
    # Ici on gere la mise à jour
    marge = 50
    if vaisseau["moveToRight"]:
        if vaisseau["x"] < window.get_width()-32 - marge:
            vaisseau["x"] = vaisseau["x"]+10
    if vaisseau["moveToLeft"]:
        if vaisseau["x"] > 0 + marge:
            # vaisseau["x"] -= vaisseau["x"]-10
            # Idem
            vaisseau["x"] -= 10

    for bullet in vaisseau["projectilsList"]:
        bullet["y"] -= 10
        if bullet["y"] < 0:
            bullet["destroyed"] = True

    i = len(vaisseau["projectilsList"]) - 1
    while i >= 0:
        if vaisseau["projectilsList"][i]["destroyed"]:
            print('yo')
            vaisseau["projectilsList"].pop(i)
        i -= 1


def __events(gameInfo):
    # Ici on gere les evenements
    for event in pygame.event.get():
        # Evenement de fermeture de la fenetre
        if event.type == pygame.QUIT:
            gameInfo["done"] = True
        # Evenement de touche du clavier appuyée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vaisseau["moveToRight"] = True
            if event.key == pygame.K_LEFT:
                vaisseau["moveToLeft"] = True
            if event.key == pygame.K_SPACE:
                bullet = projectil.copy()
                bullet["x"] = vaisseau["x"]
                bullet["y"] = vaisseau["y"]
                vaisseau["projectilsList"].append(bullet)
        # Evenement de touche du clavier relachée
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vaisseau["moveToRight"] = False
            if event.key == pygame.K_LEFT:
                vaisseau["moveToLeft"] = False


def drawGameScreen(window, gameInfo):
    __events(gameInfo)
    __update(window)
    __draw(window, gameInfo)
