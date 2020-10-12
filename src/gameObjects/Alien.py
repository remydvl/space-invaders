# alien
import pygame
from .AShip import AShip
from config.game import ALIEN_LIFES

aliensImages = {
    "1_0": pygame.image.load("./assets/images/level-1/alien_1_0.png"),
    "1_1": pygame.image.load("./assets/images/level-1/alien_1_1.png"),
    "2_0": pygame.image.load("./assets/images/level-1/alien_2_0.png"),
    "2_1": pygame.image.load("./assets/images/level-1/alien_2_1.png")
}


def getAlienImage(type, animation):
    return aliensImages[str(type) + "_" + str(animation)]


class Alien(AShip):
    def __init__(self, x, y, type):
        self.__animation = 0
        self.__type = type
        super().__init__(
            x,
            y,
            32,
            32,
            ALIEN_LIFES,
            getAlienImage(self.__type, self.__animation)
        )

    def setAnimation(self):
        if self.__animation == 0:
            self.__animation = 1
        else:
            self.__animation = 0
        self.setImage(getAlienImage(self.__type, self.__animation))
