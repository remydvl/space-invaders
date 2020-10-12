import pygame
import time
from .AGameObject import AGameObject
from config.game import PROJECTIL_TIME_BEFORE_DESTROY

playerShootImage = pygame.image.load(
    "./assets/images/level-1/shoot.png")

alienShootImage = pygame.image.load(
    "./assets/images/level-1/shootAlien.png")

destroyShootImage = pygame.image.load(
    "./assets/images/level-1/explosion.png")


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
        self.setImage(destroyShootImage)
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
    def __init__(self, x, y,):
        super().__init__(x, y, 6, 12, alienShootImage)


class PlayerProjectil(AProjectil):
    def __init__(self, x, y,):
        super().__init__(x, y, 6, 12, playerShootImage)
