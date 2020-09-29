import pygame
from introScreen import drawIntroScreen
from homeScreen import drawHomeScreen

window = pygame.display.set_mode((800, 600))
done = False

# titre de la fenetre

pygame.display.set_caption("Space Invaders")

gameState = 'intro'

while not done:
    pygame.draw.rect(window, (0, 0, 0),
                     (0, 0, window.get_width(), window.get_height()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if gameState == "intro":
                gameState = "home"

    if gameState == "intro":
        drawIntroScreen(window)
    elif gameState == "home":
        drawHomeScreen(window)

    pygame.display.flip()
