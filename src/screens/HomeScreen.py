import pygame
from config.game import GAME_STATES

pygame.font.init()


class HomeScreen:
    def __init__(self, app):
        self.__startTextFont = pygame.font.SysFont('Comic Sans MS', 50)

        self.__playText = self.__startTextFont.render(
            'Play', False, (255, 255, 255))
        self.__optionText = self.__startTextFont.render(
            'Options', False, (255, 255, 255))
        self.__returnText = self.__startTextFont.render(
            'Return', False, (255, 255, 255))

    def draw(self, app):
        xText = app.getWindow().get_width() / 2 - self.__optionText.get_width() / 2

        app.getWindow().blit(self.__playText, (xText, 200))
        app.getWindow().blit(self.__optionText, (xText, 300))
        app.getWindow().blit(self.__returnText, (xText, 400))

    def update(self, app):
        # INFO: Not used !
        pass

    def events(self, app):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.stop()
            elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                app.setState(GAME_STATES["GAME"])
