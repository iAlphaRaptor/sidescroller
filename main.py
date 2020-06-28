import pygame, rainbow
from player import Player
from background import Background
pygame.init()

colours = rainbow.colours

SCREENWIDTH = 1280
SCREENHEIGHT = 960

size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sidescroller Game")

clock = pygame.time.Clock()
carryOn = True

def loadImage(*imgs, dest=False):
    if len(imgs) == 1:
        return pygame.image.load(imgs[0])
    else:
        for img in imgs:
            dest.append(pygame.image.load(img))

backgroundsList = [Background(pygame.transform.scale(loadImage("Images/background2.png"), (SCREENWIDTH, SCREENHEIGHT)))]
backgrounds = pygame.sprite.Group()
for background in backgroundsList:
    backgrounds.add(background)

currentBackground = pygame.sprite.GroupSingle(backgroundsList[0])
player = pygame.sprite.GroupSingle(Player("X", SCREENWIDTH, SCREENHEIGHT))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False

    keys = pygame.key.get_pressed()

    player.sprite.changeVelX(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], 4)
    player.sprite.changeVelY(player.sprite.willCollide(currentBackground.sprite.boundingRects))
    player.sprite.updateMove()

    if keys[pygame.K_UP]:
        player.sprite.jump(7)

    screen.fill(colours["WHITE"])
    currentBackground.draw(screen)
    if keys[pygame.K_s]:
        for rect in currentBackground.sprite.boundingRects:
            pygame.draw.rect(screen, colours["RED"], rect)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
