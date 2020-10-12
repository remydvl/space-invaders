import pygame
from config.game import GAME_STATES

pygame.font.init()


class FinishScreen:

    def __init__(self):
        self.__congratulationFont = pygame.font.SysFont('Comic Sans MS', 100)
        self.__returnHomeFont = pygame.font.SysFont('Comic Sans MS', 50)

        self.__congratulationText = self.__congratulationFont.render(
            'Bravo', False, (255, 255, 255))

        self.__finishText = self.__returnHomeFont.render(
            'Vous avez terminez le niveau', False, (255, 255, 255))
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
        xCongratulationText = app.getWindow().get_width(
        ) / 2 - self.__congratulationText.get_width() / 2
        yCongratulationText = app.getWindow().get_height(
        ) / 2 - self.__congratulationText.get_height() * 2

        xFinishText = app.getWindow().get_width(
        ) / 2 - self.__finishText.get_width() / 2
        yFinishText = yCongratulationText + self.__congratulationText.get_height() + 10

        xReturnHome1Text = app.getWindow().get_width() / 2 - \
            self.__returnHomeText1.get_width() / 2
        yReturnHome1Text = yFinishText + \
            self.__finishText.get_height() * 2 + 10

        xReturnHome2Text = app.getWindow().get_width() / 2 - \
            self.__returnHomeText2.get_width() / 2
        yReturnHome2Text = yReturnHome1Text + self.__returnHomeText1.get_height() + 10

        app.getWindow().blit(
            self.__congratulationText,
            (xCongratulationText, yCongratulationText)
        )
        app.getWindow().blit(self.__finishText, (xFinishText, yFinishText))
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
