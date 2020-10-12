from .AGameObject import AGameObject
from config.game import MOVE_ACTION_X, MOVE_ACTION_Y


class AShip(AGameObject):
    def __init__(self, x, y, width, height, life, image):
        super().__init__(x, y, width, height, image)
        self.__life = life
        self.__moveToLeft = False
        self.__moveToRight = False
        self.__moveToTop = False
        self.__moveToBottom = False

    def removeLife(self, damage):
        self.__life -= damage

    def isDestroyed(self):
        return self.__life <= 0

    def getMoveX(self):
        if self.__moveToLeft == True:
            return MOVE_ACTION_X['LEFT']
        elif self.__moveToRight == True:
            return MOVE_ACTION_X['RIGHT']
        else:
            return MOVE_ACTION_X['STOP']

    def getMoveY(self):
        if self.__moveToTop == True:
            return MOVE_ACTION_Y['TOP']
        elif self.__moveToBottom == True:
            return MOVE_ACTION_Y['BOTTOM']
        else:
            return MOVE_ACTION_X['STOP']

    def moveX(self, moveX):
        if moveX == MOVE_ACTION_X['LEFT']:
            self.__moveToLeft = True
            self.__moveToRight = False
        elif moveX == MOVE_ACTION_X['RIGHT']:
            self.__moveToRight = True
            self.__moveToLeft = False
        elif moveX == MOVE_ACTION_X['STOP_LEFT']:
            self.__moveToLeft = False
        elif moveX == MOVE_ACTION_X['STOP_RIGHT']:
            self.__moveToRight = False

    def moveY(self, moveY):
        if moveY == MOVE_ACTION_Y['TOP']:
            self.__moveToTop = True
            self.__moveToBottom = False
        elif moveY == MOVE_ACTION_Y['BOTTOM']:
            self.__moveToBottom = True
            self.__moveToTop = False
        elif moveY == MOVE_ACTION_Y['STOP_TOP']:
            self.__moveToTop = False
        elif moveY == MOVE_ACTION_Y['STOP_BOTTOM']:
            self.__moveToBottom = False
