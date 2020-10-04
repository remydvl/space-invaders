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

init = False

pygame.font.init()

startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

# vaisseau
vaisseauBase = {
    "moveToRight": False,
    "moveToLeft": False,
    "x": 400,
    "y": 550,
    "width": 32,
    "height": 32,
    "life": 3,
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

vaisseauImage = pygame.image.load(
    getImage("../assets/images/level-1/vaisseau.png"))

# projectil aliens
projectilAlien = {
    "image": pygame.image.load(getImage("../assets/images/level-1/shootAlien.png")),
    "x": 0,
    "y": 0,
    "width": 6,
    "height": 12,
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
    "width": 32,
    "height": 32
}

vaisseau = {}

aliensList = []


def __initGame():
    global init, vaisseau, aliensList, aliensMoveX, aliensMoveY, aliensLastXDirection, aliensDirection, aliensAnimation
    init = True

    aliensMoveX = 0
    aliensMoveY = 0
    aliensLastXDirection = "RIGHT"
    aliensDirection = "RIGHT"
    aliensAnimation = 0

    aliensList = []

    col = 16
    row = 5

    rowCounter = 0
    while rowCounter < row:
        colCounter = 0
        while colCounter < col:
            alienSpace = 10
            screenMarge = 50
            newAlien = copy.deepcopy(alienBase)
            newAlien["x"] = (newAlien["width"] + alienSpace) * \
                colCounter + screenMarge
            newAlien["y"] = (newAlien["height"] + alienSpace) * rowCounter
            newAlien["type"] = (rowCounter % 2) + 1
            aliensList.append(newAlien)
            colCounter += 1
        rowCounter += 1

        vaisseau = copy.deepcopy(vaisseauBase)


aliensAnimationTime = time.time()
aliensShootTime = time.time()


def __draw(window, gameInfo):
    # Ici on dessine l'ecran de jeu

    # Vaisseau
    window.blit(vaisseauImage, (vaisseau["x"], vaisseau["y"]))

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


def __update(window, gameInfo):
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
        bullet["x"] = randomAlien["x"] + aliensMoveX + (randomAlien["width"]/2)
        bullet["y"] = randomAlien["y"] + \
            aliensMoveY + (randomAlien["height"]/2)
        randomAlien["projectilsList"].append(bullet)

        aliensShootTime = time.time()

    # Deplacement Projectiles aliens et collision vaisseau
    for alien in aliensList:
        for bullet in alien["projectilsList"]:
            bullet["y"] += ALIEN_BULLET_SPEED
            if bullet["y"] > window.get_height():
                bullet["destroyed"] = True
            elif bullet["x"] + bullet["width"] >= vaisseau["x"] and bullet["x"] <= vaisseau["x"] + vaisseau["width"]:
                if bullet["y"] + bullet["height"] >= vaisseau["y"] and bullet["y"] <= vaisseau["y"] + vaisseau["height"]:
                    bullet["destroyed"] = True
                    vaisseau["life"] -= 1

        i = len(alien["projectilsList"]) - 1
        while i >= 0:
            if alien["projectilsList"][i]["destroyed"]:
                alien["projectilsList"].pop(i)
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
                bullet = copy.copy(projectilVaisseau)
                bullet["x"] = vaisseau["x"] + (vaisseau["width"] - 6) / 2
                bullet["y"] = vaisseau["y"] + (vaisseau["height"] - 6) / 2
                vaisseau["projectilsList"].append(bullet)
        # Evenement de touche du clavier relachée
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vaisseau["moveToRight"] = False
            if event.key == pygame.K_LEFT:
                vaisseau["moveToLeft"] = False


def drawGameScreen(window, gameInfo):
    global init
    if init == False:
        __initGame()

    if vaisseau["life"] <= 0:
        gameInfo["gameState"] = 'game-over'
        init = False

    __events(gameInfo)
    __update(window, gameInfo)
    __draw(window, gameInfo)
