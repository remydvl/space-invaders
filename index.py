import pygame
from introScreen import drawIntroScreen
from homeScreen import drawHomeScreen
from GameScreen import drawGameScreen

window = pygame.display.set_mode((800, 600))

gameInfo = {
    "done": False,
    "gameState": 'intro'
}

# titre de la fenetre

pygame.display.set_caption("Space Invaders")

while not gameInfo["done"]:
    pygame.draw.rect(window, (0, 0, 0),
                     (0, 0, window.get_width(), window.get_height()))

    if gameInfo["gameState"] == "intro":
        drawIntroScreen(window, gameInfo)
    elif gameInfo["gameState"] == "home":
        drawHomeScreen(window, gameInfo)

    elif gameInfo["gameState"] == "game":
        drawGameScreen(window, gameInfo)

    pygame.display.flip()
