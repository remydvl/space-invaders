# alien
import pygame
from .AShip import AShip
from config.game import ALIEN_LIFES
from config.level import ALIENS_IMAGES_LEVEL


def getAlienImage(type, animation, gameLevel):
    return ALIENS_IMAGES_LEVEL[gameLevel - 1][str(type) + "_" + str(animation)]


class Alien(AShip):
    def __init__(self, x, y, type, gameLevel):
        self.__animation = 0
        self.__type = type
        self.__gameLevel = gameLevel
        super().__init__(
            x,
            y,
            32,
            32,
            ALIEN_LIFES,
            getAlienImage(self.__type, self.__animation, self.__gameLevel)
        )

    def setAnimation(self):
        if self.__animation == 0:
            self.__animation = 1
        else:
            self.__animation = 0
        self.setImage(getAlienImage(
            self.__type, self.__animation, self.__gameLevel))

    def getType(self):
        return self.__type
