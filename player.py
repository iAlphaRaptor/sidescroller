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
        self.rect.x = 0
        self.rect.y = 0

        self.velX = 0
        self.velY = 0
        self.colliding = False

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

    def changeVelY(self, colliding):
        if not colliding:
            self.velY += 0.5
        elif self.velY > 0:
            self.velY = 0

    def jump(self, bounce):
        if self.colliding:
            self.velY = -bounce

    def willCollide(self, collisionRects):
        tempRect = self.rect
        tempRect.x += self.velX
        tempRect.y += self.velY

        for rectangle in collisionRects:
            if tempRect.colliderect(rectangle):
                self.colliding = True
                return True
        else:
            self.colliding = False
            return False
