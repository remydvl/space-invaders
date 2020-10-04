import pygame
from screens.introScreen import drawIntroScreen
from screens.homeScreen import drawHomeScreen
from screens.gameScreen import drawGameScreen
from screens.gameOverScreen import drawGameOverScreen


window = pygame.display.set_mode((800, 600))

# gameState = 'intro' OU 'home' OU 'game' OU 'game-over'

gameInfo = {
    "done": False,
    "gameState": 'intro'
}

# titre de la fenetre

pygame.display.set_caption("Space Invaders")

while not gameInfo["done"]:
    pygame.draw.rect(
        window, (0, 0, 0),
        (0, 0, window.get_width(), window.get_height()))

    if gameInfo["gameState"] == "intro":
        drawIntroScreen(window, gameInfo)
    elif gameInfo["gameState"] == "home":
        drawHomeScreen(window, gameInfo)

    elif gameInfo["gameState"] == "game":
        drawGameScreen(window, gameInfo)
    elif gameInfo["gameState"] == "game-over":
        drawGameOverScreen(window, gameInfo)

    pygame.display.flip()
