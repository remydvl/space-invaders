import pygame

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# titre de la fenetre

pygame.display.set_caption("Space Invaders")

# creation de l'image de fond

backgroundImage = pygame.image.load("./assets/start.jpg")

# creation des textes

titleFont = pygame.font.SysFont('Comic Sans MS', 40)

startTextFont = pygame.font.SysFont('Comic Sans MS', 30)

title = titleFont.render('Space Invaders', False, (255, 255, 255))

startText = startTextFont.render('to play', False, (255, 255, 255))

startText.set_alpha(254)

goToAlpha = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if goToAlpha:
        startText.set_alpha(startText.get_alpha()-1)
        if startText.get_alpha() == 0:
            goToAlpha = False
    else:
        startText.set_alpha(startText.get_alpha()+1)
        if startText.get_alpha() >= 254:
            goToAlpha = True
    screen.blit(backgroundImage, (-235, -200))
    screen.blit(title, (250, 0))
    screen.blit(startText, (350, SCREEN_HEIGHT-100))
    pygame.display.flip()
