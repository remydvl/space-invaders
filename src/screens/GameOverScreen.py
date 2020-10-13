import pygame
from config.game import GAME_STATES

pygame.font.init()


class GameOverScreen:

    def __init__(self, app):
        self.__gameOverFont = pygame.font.SysFont('Comic Sans MS', 100)
        self.__returnHomeFont = pygame.font.SysFont('Comic Sans MS', 50)

        self.__gameOverText = self.__gameOverFont.render(
            'Game Over', False, (255, 255, 255))

        self.__returnHomeText1 = self.__returnHomeFont.render(
            'Appuyez sur la touche entrée', False, (255, 255, 255))
        self.__returnHomeText2 = self.__returnHomeFont.render(
            'pour revenir à l\'accueil', False, (255, 255, 255))
        self.__isPressed = False

        self.__goToAlpha = True
        self.__returnHomeText1.set_alpha(254)
        self.__returnHomeText2.set_alpha(254)

    def draw(self, app):
        # Ici je centre la position en X du texte
        xGameOverText = app.getWindow().get_width() / 2 - \
            self.__gameOverText.get_width() / 2
        yGameOverText = app.getWindow().get_height() / 2 - \
            self.__gameOverText.get_height() / 2

        xReturnHome1Text = app.getWindow().get_width() / 2 - \
            self.__returnHomeText1.get_width() / 2
        yReturnHome1Text = yGameOverText + self.__gameOverText.get_height() + 10

        xReturnHome2Text = app.getWindow().get_width() / 2 - \
            self.__returnHomeText2.get_width() / 2
        yReturnHome2Text = yReturnHome1Text + self.__returnHomeText1.get_height() + 10

        app.getWindow().blit(self.__gameOverText, (xGameOverText, yGameOverText))
        app.getWindow().blit(
            self.__returnHomeText1,
            (xReturnHome1Text, yReturnHome1Text))
        app.getWindow().blit(
            self.__returnHomeText2,
            (xReturnHome2Text, yReturnHome2Text))

    def update(self, app):
        # INFO: Not used !
        self.__checkTextAlpha()

    def events(self, app):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.stop()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.__isPressed = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                if self.__isPressed:
                    isPressed = False
                    app.setState(GAME_STATES["HOME"])

    def __checkTextAlpha(self):
        if self.__goToAlpha:
            self.__returnHomeText1.set_alpha(
                self.__returnHomeText1.get_alpha()-1)
            self.__returnHomeText2.set_alpha(
                self.__returnHomeText1.get_alpha())
            if self.__returnHomeText1.get_alpha() == 0:
                self.__goToAlpha = False
        else:
            self.__returnHomeText1.set_alpha(
                self.__returnHomeText1.get_alpha()+1)
            self.__returnHomeText2.set_alpha(
                self.__returnHomeText1.get_alpha())
            if self.__returnHomeText1.get_alpha() >= 254:
                self.__goToAlpha = True
