import pygame
from .AGameObject import AGameObject

playerShootImage = pygame.image.load(
    "./assets/images/level-1/shoot.png")

alienShootImage = pygame.image.load(
    "./assets/images/level-1/shootAlien.png")


class AProjectil(AGameObject):

    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.__destroyed = False

    def isDestroyed(self):
        return self.__destroyed

    def destroy(self):
        self.__destroyed = True


class AlienProjectil(AProjectil):
    def __init__(self, x, y,):
        super().__init__(x, y, 6, 12, alienShootImage)


class PlayerProjectil(AProjectil):
    def __init__(self, x, y,):
        super().__init__(x, y, 6, 12, playerShootImage)
