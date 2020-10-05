import pygame

pygame.font.init()

gameOverFont = pygame.font.SysFont('Comic Sans MS', 100)
returnHomeFont = pygame.font.SysFont('Comic Sans MS', 50)

gameOverText = gameOverFont.render('Game Over', False, (255, 255, 255))

returnHomeText1 = returnHomeFont.render(
    'Appuyez sur une touche', False, (255, 255, 255))
returnHomeText2 = returnHomeFont.render(
    'pour revenir à l\'accueil', False, (255, 255, 255))

isPressed = False


def drawGameOverScreen(window, gameInfo):
    global isPressed
    # Ici je centre la position en X du texte
    xGameOverText = window.get_width() / 2 - gameOverText.get_width() / 2
    yGameOverText = window.get_height() / 2 - gameOverText.get_height() / 2

    xReturnHome1Text = window.get_width() / 2 - returnHomeText1.get_width() / 2
    yReturnHome1Text = yGameOverText + gameOverText.get_height() + 10

    xReturnHome2Text = window.get_width() / 2 - returnHomeText2.get_width() / 2
    yReturnHome2Text = yReturnHome1Text + returnHomeText1.get_height() + 10

    window.blit(gameOverText, (xGameOverText, yGameOverText))
    window.blit(returnHomeText1, (xReturnHome1Text, yReturnHome1Text))
    window.blit(returnHomeText2, (xReturnHome2Text, yReturnHome2Text))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameInfo["done"] = True
        elif event.type == pygame.KEYDOWN:
            isPressed = True
        elif event.type == pygame.KEYUP:
            if isPressed:
                isPressed = False
                gameInfo["gameState"] = "home"
