from config.game import GAME_STATES
import pygame

pygame.font.init()


class IntroScreen:
    def __init__(self):
        self.__titleFont = titleFont = pygame.font.SysFont('Comic Sans MS', 80)
        self.__startTextFont = pygame.font.SysFont('Comic Sans MS', 60)
        self.__title = titleFont.render(
            'Space Invaders', False, (255, 255, 255))
        self.__startText = self.__startTextFont.render(
            'to play', False, (255, 255, 255))
        self.__backgroundImage = pygame.image.load(
            './assets/images/menu/start.jpg')

        self.__goToAlpha = True
        self.__startText.set_alpha(254)

    def draw(self, app):
        xTitle = app.getWindow().get_width() / 2 - self.__title.get_width() / 2
        yTitle = 50

        xStartText = app.getWindow().get_width() / 2 - self.__startText.get_width() / 2
        yStartText = app.getWindow().get_height() - 75

        app.getWindow().blit(self.__backgroundImage, (-235, -200))
        app.getWindow().blit(self.__title, (xTitle, yTitle))
        app.getWindow().blit(self.__startText, (xStartText, yStartText))

    def update(self, app):
        self.__checkTextAlpha()

    def events(self, app):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.stop()
            elif event.type == pygame.KEYUP:
                app.setState(GAME_STATES["HOME"])

    def __checkTextAlpha(self):
        if self.__goToAlpha:
            self.__startText.set_alpha(
                self.__startText.get_alpha()-1)
            if self.__startText.get_alpha() == 0:
                self.__goToAlpha = False
        else:
            self.__startText.set_alpha(
                self.__startText.get_alpha()+1)
            if self.__startText.get_alpha() >= 254:
                self.__goToAlpha = True
