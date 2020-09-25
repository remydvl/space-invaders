import pygame

SCREEN_WIDTH=800

SCREEN_HEIGHT=600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

pygame.display.set_caption("Space Invaders")

titleFont = pygame.font.SysFont('Comic Sans MS', 40)

startTextFont = pygame.font.SysFont('Comic Sans MS', 30)

title = titleFont.render('Space Invaders', False, (255, 255, 255))

startText = startTextFont.render('Appuyer sur une touche pour jouer', False, (255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(title, (250, 0))
    screen.blit(startText, (150, SCREEN_HEIGHT-100))
    pygame.display.flip()
