import pygame
import time
import random
import copy
from utils.images import getImage

# ICI on definis la config du jeu
ALIENS_ANIMATION_TIME = 1.000
ALIENS_SHOOT_TIME = 1.000
ALIENS_ANIMATION_MOVE = 10
ALIENS_MAX_RIGHT = 50

VAISSEAU_BULLET_SPEED = 5
ALIEN_BULLET_SPEED = 2

pygame.font.init()

startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

# vaisseau
vaisseau = {
    "image": pygame.image.load(getImage("../assets/images/level-1/vaisseau.png")),
    "moveToRight": False,
    "moveToLeft": False,
    "x": 400,
    "y": 550,
    "projectilsList": []
}

# projectil du vaisseau
projectilVaisseau = {
    "image": pygame.image.load(getImage("../assets/images/level-1/shoot.png")),
    "x": 0,
    "y": 0,
    "destroyed": False
}

# alien
aliensImages = {
    "1_0": pygame.image.load(getImage("../assets/images/level-1/alien_1_0.png")),
    "1_1": pygame.image.load(getImage("../assets/images/level-1/alien_1_1.png")),
    "2_0": pygame.image.load(getImage("../assets/images/level-1/alien_2_0.png")),
    "2_1": pygame.image.load(getImage("../assets/images/level-1/alien_2_1.png"))
}

# projectil aliens
projectilAlien = {
    "image": pygame.image.load(getImage("../assets/images/level-1/shootAlien.png")),
    "x": 0,
    "y": 0,
    "destroyed": False
}

aliensMoveX = 0
aliensMoveY = 0
aliensLastXDirection = "RIGHT"
aliensDirection = "RIGHT"
aliensAnimation = 0

alienBase = {
    "type": 1,
    "x": 0,
    "y": 0,
    "projectilsList": [],
}

col = 16
row = 5

aliensList = []

rowCounter = 0
while rowCounter < row:
    colCounter = 0
    while colCounter < col:
        alienSize = 32
        alienSpace = 10
        screenMarge = 50
        newAlien = copy.deepcopy(alienBase)
        newAlien["x"] = (alienSize + alienSpace) * colCounter + screenMarge
        newAlien["y"] = (alienSize + alienSpace) * rowCounter
        newAlien["type"] = (rowCounter % 2) + 1
        aliensList.append(newAlien)
        colCounter += 1
    rowCounter += 1

aliensAnimationTime = time.time()
aliensShootTime = time.time()


def __draw(window, gameInfo):
    # Ici on dessine l'ecran de jeu

    # Vaisseau
    window.blit(vaisseau["image"], (vaisseau["x"], vaisseau["y"]))

    for bullet in vaisseau["projectilsList"]:
        window.blit(bullet["image"], (bullet["x"], bullet["y"]))

    # Aliens

    for alien in aliensList:
        alienImage = aliensImages[
            str(alien["type"]) +
            "_" +
            str(aliensAnimation)
        ]
        window.blit(
            alienImage,
            (alien["x"] + aliensMoveX, alien["y"] + aliensMoveY))

    for alien in aliensList:
        for bullet in alien["projectilsList"]:
            window.blit(
                bullet["image"],
                (bullet["x"], bullet["y"]))


def __update(window):
    global aliensAnimationTime, aliensShootTime, aliensDirection, aliensMoveX, aliensMoveY, aliensLastXDirection, aliensAnimation

    # Vaisseau
    marge = 50
    if vaisseau["moveToRight"]:
        if vaisseau["x"] < window.get_width()-32 - marge:
            vaisseau["x"] = vaisseau["x"]+10
    if vaisseau["moveToLeft"]:
        if vaisseau["x"] > 0 + marge:
            # vaisseau["x"] -= vaisseau["x"]-10
            # Idem
            vaisseau["x"] -= VAISSEAU_BULLET_SPEED

    # Projectiles Vaisseau
    for bullet in vaisseau["projectilsList"]:
        bullet["y"] -= 10
        if bullet["y"] < 0:
            bullet["destroyed"] = True

    i = len(vaisseau["projectilsList"]) - 1
    while i >= 0:
        if vaisseau["projectilsList"][i]["destroyed"]:
            vaisseau["projectilsList"].pop(i)
        i -= 1

    # aliens

    # Toute les x seconde (pour l'animation)
    if time.time() - aliensAnimationTime > ALIENS_ANIMATION_TIME:
        # Animation
        if aliensAnimation == 0:
            aliensAnimation = 1
        else:
            aliensAnimation = 0
        # Deplacement
        if aliensDirection == "RIGHT":
            aliensMoveX += ALIENS_ANIMATION_MOVE
            if aliensMoveX > ALIENS_MAX_RIGHT:
                aliensDirection = "BOTTOM"
        elif aliensDirection == "LEFT":
            aliensMoveX -= ALIENS_ANIMATION_MOVE
            if aliensMoveX < 0:
                aliensDirection = "BOTTOM"
        elif aliensDirection == "BOTTOM":
            aliensMoveY += ALIENS_ANIMATION_MOVE
            if aliensLastXDirection == "RIGHT":
                aliensDirection = "LEFT"
                aliensLastXDirection = "LEFT"
            else:
                aliensDirection = "RIGHT"
                aliensLastXDirection = "RIGHT"
        aliensAnimationTime = time.time()

    # Toute les x seconde (pour les tirs)
    if time.time() - aliensShootTime > ALIENS_SHOOT_TIME:
        randomNumber = random.randint(0, len(aliensList) - 1)
        randomAlien = aliensList[randomNumber]
        bullet = copy.copy(projectilAlien)
        bullet["x"] = randomAlien["x"] + aliensMoveX + (alienSize/2)
        bullet["y"] = randomAlien["y"] + aliensMoveY + (alienSize/2)
        randomAlien["projectilsList"].append(bullet)

        aliensShootTime = time.time()

    # Deplacement Projectiles aliens
    for alien in aliensList:
        for bullet in alien["projectilsList"]:
            bullet["y"] += ALIEN_BULLET_SPEED
            if bullet["y"] > window.get_height():
                bullet["destroyed"] = True
        i = len(alien["projectilsList"]) - 1
        while i >= 0:
            if alien["projectilsList"][i]["destroyed"]:
                alien["projectilsList"].pop(i)
            i -= 1


def __events(gameInfo):
    vaisseauSize = 32
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
                bullet = copy.copy(projectilVaisseau)
                bullet["x"] = vaisseau["x"] + (vaisseauSize - 6) / 2
                bullet["y"] = vaisseau["y"] + (vaisseauSize - 6) / 2
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
