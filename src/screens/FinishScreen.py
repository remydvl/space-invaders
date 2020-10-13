import pygame
from config.game import GAME_STATES
from config.level import MAX_LEVEL

pygame.font.init()


class FinishScreen:

    def __init__(self, app):
        self.__congratulationFont = pygame.font.SysFont('Comic Sans MS', 100)
        self.__returnHomeFont = pygame.font.SysFont('Comic Sans MS', 50)

        self.__congratulationText = self.__congratulationFont.render(
            'Bravo', False, (255, 255, 255))

        finishText = 'Vous avez terminez le niveau ' + str(app.getGameLevel())

        if app.getGameLevel() == MAX_LEVEL:
            finishText = 'Vous avez terminez tout les niveaux'

        self.__finishText = self.__returnHomeFont.render(
            finishText, False, (255, 255, 255))
        self.__continueText1 = self.__returnHomeFont.render(
            'Appuyez sur la touche entrée', False, (255, 255, 255))
        self.__continueText2 = self.__returnHomeFont.render(
            'pour continuer au niveau ' + str(app.getGameLevel() + 1), False, (255, 255, 255))

        self.__returnHomeText1 = self.__returnHomeFont.render(
            'Appuyez sur la touche echape', False, (255, 255, 255))

        self.__returnHomeText2 = self.__returnHomeFont.render(
            'pour revenir à l\'accueil', False, (255, 255, 255))
        self.__isReturnKeyPressed = False
        self.__isEscapeKeyPressed = False

        self.__goToAlpha = True
        self.__continueText1.set_alpha(254)
        self.__continueText2.set_alpha(254)
        self.__returnHomeText1.set_alpha(254)
        self.__returnHomeText2.set_alpha(254)

    def draw(self, app):
        # Ici je centre la position en X du texte
        xCongratulationText = app.getWindow().get_width(
        ) / 2 - self.__congratulationText.get_width() / 2
        yCongratulationText = app.getWindow().get_height(
        ) / 2 - self.__congratulationText.get_height() * 3

        xFinishText = app.getWindow().get_width(
        ) / 2 - self.__finishText.get_width() / 2
        yFinishText = yCongratulationText + self.__congratulationText.get_height() + 10

        xContinue1Text = app.getWindow().get_width() / 2 - \
            self.__continueText1.get_width() / 2
        yContinue1Text = yFinishText +\
            self.__finishText.get_height() * 2 + 10

        xContinue2Text = app.getWindow().get_width() / 2 - \
            self.__continueText2.get_width() / 2
        yContinue2Text = yContinue1Text + self.__continueText1.get_height() + 10

        xReturnHome1Text = app.getWindow().get_width() / 2 - \
            self.__returnHomeText1.get_width() / 2
        yReturnHome1Text = yContinue2Text + self.__continueText2.get_height() * 2 + 10

        xReturnHome2Text = app.getWindow().get_width() / 2 - \
            self.__returnHomeText2.get_width() / 2
        yReturnHome2Text = yReturnHome1Text + self.__returnHomeText1.get_height() + 10

        app.getWindow().blit(
            self.__congratulationText,
            (xCongratulationText, yCongratulationText)
        )
        app.getWindow().blit(self.__finishText, (xFinishText, yFinishText))

        if app.getGameLevel() < MAX_LEVEL:
            app.getWindow().blit(
                self.__continueText1,
                (xContinue1Text, yContinue1Text))
            app.getWindow().blit(
                self.__continueText2,
                (xContinue2Text, yContinue2Text))

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.__isReturnKeyPressed = True
                elif event.key == pygame.K_ESCAPE:
                    self.__isEscapeKeyPressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if self.__isReturnKeyPressed:
                        self.__isReturnKeyPressed = False
                        if app.getGameLevel() < MAX_LEVEL:
                            app.setGameLevel(app.getGameLevel() + 1)
                elif event.key == pygame.K_ESCAPE:
                    if self.__isEscapeKeyPressed:
                        self.__isEscapeKeyPressed = False
                        app.setState(GAME_STATES["HOME"])

    def __checkTextAlpha(self):
        if self.__goToAlpha:
            self.__continueText1.set_alpha(
                self.__continueText1.get_alpha()-1
            )
            self.__continueText2.set_alpha(
                self.__continueText1.get_alpha()
            )
            self.__returnHomeText1.set_alpha(
                self.__continueText1.get_alpha()-1
            )
            self.__returnHomeText2.set_alpha(
                self.__continueText1.get_alpha()
            )
            if self.__continueText1.get_alpha() == 0:
                self.__goToAlpha = False
        else:
            self.__continueText1.set_alpha(
                self.__continueText1.get_alpha()+1)
            self.__continueText2.set_alpha(
                self.__continueText1.get_alpha())
            self.__returnHomeText1.set_alpha(
                self.__continueText1.get_alpha()+1)
            self.__returnHomeText2.set_alpha(
                self.__continueText1.get_alpha())
            if self.__continueText1.get_alpha() >= 254:
                self.__goToAlpha = True
