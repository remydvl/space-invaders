import pygame

from config.game import MOVE_ACTION_X
from .AShip import AShip
from config.game import PLAYER_SPEED_MOVE, PLAYER_LIFES

shipImage = pygame.image.load(
    "./assets/images/level-1/vaisseau.png")


class Player(AShip):

    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, PLAYER_LIFES, shipImage)
        self.__score = 0

    def getScore(self):
        return self.__score

    def setScore(self, newScore):
        self.__score = newScore

    def update(self, app):
        screenPadding = 50
        if self.getMoveX() == MOVE_ACTION_X["RIGHT"]:
            if self.getX() < app.getWindow().get_width() - self.getWidth() - screenPadding:
                self.setX(self.getX() + PLAYER_SPEED_MOVE)
        elif self.getMoveX() == MOVE_ACTION_X["LEFT"]:
            if self.getX() > 0 + screenPadding:
                self.setX(self.getX() - PLAYER_SPEED_MOVE)
