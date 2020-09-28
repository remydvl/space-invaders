import pygame
from introScreen import drawIntroScreen
# from homeScreen import drawHomeScreen

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

pygame.font.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# titre de la fenetre

pygame.display.set_caption("Space Invaders")

gameState = 'intro'

while not done:
    pygame.draw.rect(window, (0, 0, 0),
                     (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # elif event.type == pygame.KEYUP:
            # if gameState == "intro":
            # gameState = "home"

    if gameState == "intro":
        drawIntroScreen(window)
    # elif gameState == "home":
    #    drawHomeScreen(window)

    pygame.display.flip()
