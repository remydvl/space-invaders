import pygame
import time
from .AGameObject import AGameObject
from config.game import PROJECTIL_TIME_BEFORE_DESTROY
from config.level import ALINE_SHOOT_IMAGES_LEVEL, PLAYER_SHOOT_IMAGES_LEVEL, ALIEN_SHOOT_DESTROY_IMAGES_LEVEL, PLAYER_SHOOT_DESTROY_IMAGES_LEVEL


class AProjectil(AGameObject):

    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.__destroyed = False
        self.__destroyInProcess = False
        self.__destroyTime = time.time()

    def isInDestroyProcess(self):
        return self.__destroyInProcess

    def isDestroyed(self):
        return self.__destroyed

    def destroy(self):
        self.__destroyInProcess = True
        lastWidth = self.getWidth()
        lastHeight = self.getHeight()
        self.setHeight(32)
        self.setWidth(32)
        self.setX(self.getX() - self.getWidth() / 2 + lastWidth / 2)
        self.setY(self.getY() - self.getHeight() / 2 + lastHeight / 2)
        self.__destroyTime = time.time()

    def draw(self, window):
        if self.isInDestroyProcess() and time.time() - self.__destroyTime > PROJECTIL_TIME_BEFORE_DESTROY:
            self.__destroyed = True
        super().draw(window)


class AlienProjectil(AProjectil):
    def __init__(self, x, y, gameLevel, alienType=0):
        super().__init__(
            x,
            y,
            6,
            12,
            ALINE_SHOOT_IMAGES_LEVEL[gameLevel - 1][alienType - 1]
        )
        self.__gameLevel = gameLevel
        self.__type = alienType

    def destroy(self):
        self.setImage(
            ALIEN_SHOOT_DESTROY_IMAGES_LEVEL[self.__gameLevel - 1][self.__type - 1])
        super().destroy()


class PlayerProjectil(AProjectil):
    def __init__(self, x, y, gameLevel):
        self.__gameLevel = gameLevel
        super().__init__(x, y, 6, 12, PLAYER_SHOOT_IMAGES_LEVEL[gameLevel - 1])

    def destroy(self):
        self.setImage(
            PLAYER_SHOOT_DESTROY_IMAGES_LEVEL[self.__gameLevel - 1])
        super().destroy()
