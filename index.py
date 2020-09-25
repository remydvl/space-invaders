import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

pygame.display.set_caption("Space Invaders")

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Space Invaders, Appuyer sur une touche pour jouer', False, (255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(textsurface, (0, 0))
    pygame.display.flip()
