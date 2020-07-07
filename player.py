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
        self.rect.x = 150
        self.rect.y = 0

        self.velX = 0
        self.velY = 0
        self.colliding = []

        self.image.blit(manImage, (0, 0))

    def updateMove(self):
        """Updates the position of the sprite using its current velocity in each direction."""
        self.rect.x += self.velX
        self.rect.y += self.velY

    def changeVelX(self, direction, pixels):
        ##print(self.colliding)
        if direction > 0:
            if "RIGHT" not in self.colliding:
                self.velX = pixels
            else:
                self.velX = 0
        elif direction < 0:
            if "LEFT" not in self.colliding:
                self.velX = -pixels
            else:
                self.velX = 0
        else:
            self.velX = 0

    def changeVelY(self, colliding):
        if "BOTTOM" not in self.colliding and "TOP" not in self.colliding:
            self.velY += 0.5
        else:
            self.velY = 0

    def jump(self, bounce):
        if "BOTTOM" in self.colliding and self.velY == 0:
            self.velY = -bounce

    def willCollide(self, collisionRects):
        self.colliding = []

        tempRect = pygame.sprite.Sprite()
        tempRect.image = pygame.Surface([self.size[0], self.size[1]])
        tempRect.rect = tempRect.image.get_rect()
        tempRect.rect.x = self.rect.x + self.velX
        tempRect.rect.y = self.rect.y + self.velY

        tempRectGroup = pygame.sprite.Group(tempRect)

        collidingWith = pygame.sprite.groupcollide(tempRectGroup, collisionRects, False, False)
        if len(collidingWith) > 0:
            for collisionRect in list(collidingWith.values())[0]:
                if collisionRect.rect.right >= self.rect.x:
                    self.colliding.append("LEFT")
                if collisionRect.rect.x <= self.rect.right:
                    self.colliding.append("RIGHT")
                if collisionRect.rect.y >= self.rect.y + self.size[1] - 1:
                    self.colliding.append("BOTTOM")
                if collisionRect.rect.y < self.rect.y:
                    self.colliding.append("TOP")
            return True

        return False
