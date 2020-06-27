import pygame, rainbow
from player import Player
pygame.init()

colours = rainbow.colours

SCREENWIDTH = 1280
SCREENHEIGHT = 960

size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sidescroller Game")
clock = pygame.time.Clock()

carryOn = True

player = pygame.sprite.GroupSingle(Player("X", SCREENWIDTH, SCREENHEIGHT))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.sprite.jump(15)

    player.sprite.changeVelX(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], 5)
    player.sprite.changeVelY()
    player.sprite.updateMove()

    screen.fill(colours["WHITE"])
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
