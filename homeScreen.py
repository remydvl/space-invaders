import pygame

pygame.font.init()

startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

playText = startTextFont.render('Play', False, (255, 255, 255))
optionText = startTextFont.render('Options', False, (255, 255, 255))
returnText = startTextFont.render('Return', False, (255, 255, 255))


def drawHomeScreen(window):
    # Ici je centre la position en X des textes
    xText = window.get_width() / 2 - optionText.get_width() / 2

    window.blit(playText, (xText, 200))
    window.blit(optionText, (xText, 300))
    window.blit(returnText, (xText, 400))
