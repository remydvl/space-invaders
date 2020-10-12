import pygame
import time
import random
from config.game import GAME_STATES, ALIENS_ANIMATION_TIME, ALIEN_BULLET_SPEED, MOVE_ACTION_X
from config.game import ALIENS_MAX_RIGHT, ALIENS_SPEED_MOVE, ALIENS_SHOOT_TIME
from gameObjects import Player, Alien, AlienProjectil, PlayerProjectil

pygame.font.init()


class GameScreen:
    def __init__(self, app):
        self.__scoreFont = pygame.font.SysFont('Comic Sans MS', 50)
        self.__aliensMoveX = 0
        self.__aliensMoveY = 0
        self.__aliensLastXDirection = "RIGHT"
        self.__aliensDirection = "RIGHT"
        aliensAnimation = 0
        self.__player = Player(0, 0)
        self.__player.setX(
            app.getWindow().get_width() /
            2 - self.__player.getWidth() / 2)
        self.__player.setY(
            app.getWindow().get_height() - self.__player.getHeight() * 2)
        self.__aliensList = []
        self.__initAliens()
        self.__playerProjectilsList = []
        self.__aliensProjectilsList = []
        self.__aliensAnimationTime = time.time()
        self.__aliensShootTime = time.time()

    def __initAliens(self):
        col = 16
        row = 5

        rowCounter = 0
        while rowCounter < row:
            colCounter = 0
            while colCounter < col:
                alienSpace = 10
                screenMarge = 50
                newAlien = Alien(0, 0, (rowCounter % 2) + 1)
                newAlien.setX(
                    (newAlien.getWidth() + alienSpace) *
                    colCounter + screenMarge)
                newAlien.setY((newAlien.getHeight() + alienSpace) * rowCounter)
                self.__aliensList.append(newAlien)
                colCounter += 1
            rowCounter += 1

    def draw(self, app):

        self.__player.draw(app.getWindow())
        for bullet in self.__playerProjectilsList:
            bullet.draw(app.getWindow())
        for alien in self.__aliensList:
            alien.draw(
                app.getWindow(),
                {
                    "x": self.__aliensMoveX,
                    "y": self.__aliensMoveY
                }
            )

        for bullet in self.__aliensProjectilsList:
            bullet.draw(app.getWindow())

        app.getWindow().blit(
            self.__scoreFont.render(
                str(self.__player.getScore()), False, (255, 255, 255)),
            (0, 0)
        )

    def update(self, app):
        if self.__player.isDestroyed():
            app.setState(GAME_STATES['GAME_OVER'])
        if len(self.__aliensList) == 0:
            app.setState(GAME_STATES['FINISH'])

        # Vaisseau
        self.__player.update(app)

        # Projectiles Vaisseau
        for bullet in self.__playerProjectilsList:
            bullet.setY(bullet.getY() - 10)
            if bullet.getY() < 0:
                bullet.destroy()

        i = len(self.__playerProjectilsList) - 1
        while i >= 0:
            if self.__playerProjectilsList[i].isDestroyed():
                self.__playerProjectilsList.pop(i)
            i -= 1

        # aliens

        # Toute les x seconde (pour l'animation)
        if time.time() - self.__aliensAnimationTime > ALIENS_ANIMATION_TIME:
            if self.__aliensDirection == "RIGHT":
                self.__aliensMoveX += ALIENS_SPEED_MOVE
                if self.__aliensMoveX > ALIENS_MAX_RIGHT:
                    self.__aliensDirection = "BOTTOM"
            elif self.__aliensDirection == "LEFT":
                self.__aliensMoveX -= ALIENS_SPEED_MOVE
                if self.__aliensMoveX < 0:
                    self.__aliensDirection = "BOTTOM"
            elif self.__aliensDirection == "BOTTOM":
                self.__aliensMoveY += ALIENS_SPEED_MOVE
                if self.__aliensLastXDirection == "RIGHT":
                    self.__aliensDirection = "LEFT"
                    self.__aliensLastXDirection = "LEFT"
                else:
                    self.__aliensDirection = "RIGHT"
                    self.__aliensLastXDirection = "RIGHT"
            for alien in self.__aliensList:
                alien.setAnimation()
            self.__aliensAnimationTime = time.time()

        # Toute les x seconde (pour les tirs)
        if len(self.__aliensList) > 0 and time.time() - self.__aliensShootTime > ALIENS_SHOOT_TIME:
            randomNumber = random.randint(0, len(self.__aliensList) - 1)
            randomAlien = self.__aliensList[randomNumber]
            bullet = AlienProjectil(
                randomAlien.getX() + self.__aliensMoveX + (randomAlien.getWidth() / 2),
                randomAlien.getY() + self.__aliensMoveY + (randomAlien.getHeight() / 2)
            )
            self.__aliensProjectilsList.append(bullet)

            self.__aliensShootTime = time.time()

        i = len(self.__aliensList) - 1
        while i >= 0:
            if self.__aliensList[i].isDestroyed():
                self.__aliensList.pop(i)
            i -= 1

        # Deplacement Projectiles aliens et collision vaisseau
        for alien in self.__aliensList:
            for bullet in self.__playerProjectilsList:
                if bullet.getX() + bullet.getWidth() >= alien.getX() + self.__aliensMoveX and bullet.getX() <= alien.getX() + self.__aliensMoveX + alien.getWidth():
                    if bullet.getY() + bullet.getHeight() >= alien.getY() + self.__aliensMoveY and bullet.getY() <= alien.getY() + self.__aliensMoveY + alien.getHeight():
                        bullet.destroy()
                        alien.removeLife(1)
                        self.__player.setScore(self.__player.getScore() + 10)

        for bullet in self.__aliensProjectilsList:
            bullet.setY(bullet.getY() + ALIEN_BULLET_SPEED)
            if bullet.getY() > app.getWindow().get_height():
                bullet.destroy()
            elif bullet.getX() + bullet.getWidth() >= self.__player.getX() and bullet.getX() <= self.__player.getX() + self.__player.getWidth():
                if bullet.getY() + bullet.getHeight() >= self.__player.getY() and bullet.getY() <= self.__player.getY() + self.__player.getHeight():
                    bullet.destroy()
                    self.__player.removeLife(1)

        i = len(self.__aliensProjectilsList) - 1
        while i >= 0:
            if self.__aliensProjectilsList[i].isDestroyed():
                self.__aliensProjectilsList.pop(i)
            i -= 1

    def events(self, app):
        # Ici on gere les evenements
        for event in pygame.event.get():
            # Evenement de fermeture de la fenetre
            if event.type == pygame.QUIT:
                app.stop()
            # Evenement de touche du clavier appuyée
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.__player.moveX(MOVE_ACTION_X["RIGHT"])
                if event.key == pygame.K_LEFT:
                    self.__player.moveX(MOVE_ACTION_X["LEFT"])
                if event.key == pygame.K_SPACE:
                    bullet = PlayerProjectil(0, 0)
                    bullet.setX(
                        self.__player.getX() +
                        (self.__player.getWidth() - bullet.getWidth()) / 2
                    )
                    bullet.setY(
                        self.__player.getY() +
                        (self.__player.getHeight() - bullet.getHeight()) / 2
                    )
                    self.__playerProjectilsList.append(bullet)
            # Evenement de touche du clavier relachée
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.__player.moveX(MOVE_ACTION_X["STOP_RIGHT"])
                if event.key == pygame.K_LEFT:
                    self.__player.moveX(MOVE_ACTION_X["STOP_LEFT"])
