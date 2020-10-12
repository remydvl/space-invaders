
import pygame
from screens import IntroScreen, HomeScreen, GameScreen, GameOverScreen, FinishScreen
from config.game import GAME_STATES, FPS


class Application():

    def __init__(self):
        self.__window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.__run = False
        self.__actualScreen = IntroScreen()
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

    def setState(self, state):
        if state == GAME_STATES["INTRO"]:
            self.__actualScreen = IntroScreen()
        elif state == GAME_STATES["HOME"]:
            self.__actualScreen = HomeScreen()
        elif state == GAME_STATES["GAME"]:
            self.__actualScreen = GameScreen(self)
        elif state == GAME_STATES["GAME_OVER"]:
            self.__actualScreen = GameOverScreen()
        elif state == GAME_STATES["FINISH"]:
            self.__actualScreen = FinishScreen()

        else:
            print('[setStateError]: the state "', state, '" does not exist !')
            self.stop()
