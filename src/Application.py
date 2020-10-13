
import pygame
from screens import IntroScreen, HomeScreen, GameScreen, GameOverScreen, FinishScreen
from config.game import GAME_STATES, FPS
from config.level import MAX_LEVEL


class Application():

    def __init__(self):
        self.__window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.__run = False
        self.__gameLevel = 1
        self.__actualScreen = IntroScreen(self)
        self.__clock = pygame.time.Clock()

    def run(self):
        self.__run = True
        while self.__run:
            self.__clock.tick(FPS)
            pygame.draw.rect(
                self.__window, (0, 0, 0),
                (0, 0, self.__window.get_width(), self.__window.get_height()))

            self.__actualScreen.events(self)
            self.__actualScreen.update(self)
            self.__actualScreen.draw(self)

            pygame.display.flip()

    def getWindow(self):
        return self.__window

    def stop(self):
        self.__run = False

    def getGameLevel(self):
        return self.__gameLevel

    def setGameLevel(self, newLevel):
        if newLevel <= MAX_LEVEL and newLevel > 0:
            self.__gameLevel = newLevel
            self.setState(GAME_STATES["GAME"])
        else:
            print(
                '[setGameLevel]: the level "', newLevel,
                '" is not available ! You are redirect on Intro Screen'
            )
            self.__gameLevel = 1
            self.setState(GAME_STATES["INTRO"])

    def setState(self, state):
        if state == GAME_STATES["INTRO"]:
            self.__actualScreen = IntroScreen(self)
        elif state == GAME_STATES["HOME"]:
            self.__actualScreen = HomeScreen(self)
        elif state == GAME_STATES["GAME"]:
            self.__actualScreen = GameScreen(self)
        elif state == GAME_STATES["GAME_OVER"]:
            self.__actualScreen = GameOverScreen(self)
        elif state == GAME_STATES["FINISH"]:
            self.__actualScreen = FinishScreen(self)

        else:
            print('[setStateError]: the state "', state, '" does not exist !')
            self.stop()
