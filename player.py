import pygame
from rainbow import colours
pygame.init()

class Player(pygame.sprite.Sprite):
    """Class for the main player sprite.
    Name - Name of the player
    screenX - Width of the game screen
    screenY - Height of the game screen"""

    def __init__(self, name, screenX, screenY):
        super().__init__()

        self.name = name
        self.money = 100
        self.pos = 3

        self.screenX = screenX
        self.screenY = screenY

        self.size = [int(screenX / 17), int(screenY / 6.4)]

        imageLoad = pygame.image.load("Images/stickman.png")
        manImage = pygame.transform.scale(imageLoad, (self.size[0], self.size[1]))

        self.image = pygame.Surface(self.size)
        self.image.fill(colours["WHITE"])
        self.image.set_colorkey(colours["WHITE"])

        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250

        self.velX = 0
        self.velY = 0

        self.image.blit(manImage, (0, 0))

    def updateMove(self):
        """Updates the position of the sprite using its current velocity in each direction."""
        self.rect.x += self.velX
        self.rect.y += self.velY

    def changeVelX(self, direction, pixels):
        if direction > 0:
            self.velX = pixels
        elif direction < 0:
            self.velX = -pixels
        else:
            self.velX = 0

    def changeVelY(self):
        if self.rect.y < self.screenY - self.size[1]:
            self.velY += 1
        elif self.velY > 0:
            self.velY = 0

    def jump(self, bounce):
        if self.rect.y >= self.screenY - self.size[1]:
            self.velY = -bounce
