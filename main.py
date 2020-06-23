import pygame, rainbow
pygame.init()

colours = rainbow.colours

SCREENWIDTH = 1280
SCREENHEIGHT = 960
size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sidescroller Game")
clock = pygame.time.Clock()

carryOn = True

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
