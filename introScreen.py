import pygame

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

pygame.font.init()

print()

titleFont = pygame.font.SysFont('Comic Sans MS', 80)
startTextFont = pygame.font.SysFont('Comic Sans MS', 60)

title = titleFont.render('Space Invaders', False, (255, 255, 255))
startText = startTextFont.render('to play', False, (255, 255, 255))
backgroundImage = pygame.image.load("./assets/start.jpg")

goToAlpha = True


startText.set_alpha(254)


def _checkTextAlpha():
    global goToAlpha

    if goToAlpha:
        startText.set_alpha(
            startText.get_alpha()-1)
        if startText.get_alpha() == 0:
            goToAlpha = False
    else:
        startText.set_alpha(
            startText.get_alpha()+1)
        if startText.get_alpha() >= 254:
            goToAlpha = True


def drawIntroScreen(window, gameInfo):
    _checkTextAlpha()

    # Ici je centre la position en X des textes
    xTitle = window.get_width() / 2 - title.get_width() / 2
    xStartText = window.get_width() / 2 - startText.get_width() / 2

    yTitle = 50
    yStartText = window.get_height() - 75

    window.blit(backgroundImage, (-235, -200))
    window.blit(title, (xTitle, yTitle))
    window.blit(startText, (xStartText, yStartText))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameInfo["done"] = True
        elif event.type == pygame.KEYUP:
            gameInfo["gameState"] = "home"