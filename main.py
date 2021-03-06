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

def loadImage(*imgs):
    if len(imgs) == 1:
        return pygame.image.load(imgs[0])
    else:
        temp = []
        for img in imgs:
            temp.append(pygame.image.load(img))
        return temp

backgroundsList = [Background(pygame.transform.scale(loadImage("Images/background5.png"), (SCREENWIDTH, SCREENHEIGHT)))]
backgrounds = pygame.sprite.Group()
for background in backgroundsList:
    backgrounds.add(background)

currentBackground = pygame.sprite.GroupSingle(backgroundsList[0])
player = pygame.sprite.GroupSingle(Player("X", SCREENWIDTH, SCREENHEIGHT))

while carryOn:
    print(pygame.event.get())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False

    keys = pygame.key.get_pressed()



    if keys[pygame.K_UP]:
        player.sprite.jump(12)

    player.sprite.changeVelX(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], 5)
    player.sprite.changeVelY(player.sprite.willCollide(currentBackground.sprite.boundingRects))
    player.sprite.updateMove()

    screen.fill(colours["WHITE"])
    currentBackground.draw(screen)
    if keys[pygame.K_s]:
        for rect in currentBackground.sprite.boundingRects:
            pygame.draw.rect(screen, colours["RED"], rect)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
