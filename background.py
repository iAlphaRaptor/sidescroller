import pygame, time
from rainbow import colours
from platform import Platform
pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, picture):
        super().__init__()

        self.picture = picture
        self.width, self.height = self.picture.get_size()
        self.boundingRects = self.getBoundingRects((0, 0, 0, 255))

        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        self.image.fill(colours["WHITE"])
        self.image.set_colorkey(colours["WHITE"])
        self.image.blit(self.picture, (0,0))

    def getBoundingRects(self, colour):
        """Searches through image to find rectangles of the given colour.
        Returns list of Platform objects which are used for collision detection.
        Colour should be given as a 4 number tuple with alpha included."""

        start = time.time()
        ## Gets dictionary of all rows containing pixels of the target colour.
        targetPixels = []
        for i in range(1, self.height-1, 1):
            for j in range(1, self.width-1, 1):
                if self.picture.get_at((j, i)) == colour:
                    if self.picture.get_at((j+1, i)) != colour or self.picture.get_at((j-1, i)) != colour or self.picture.get_at((j, i+1)) != colour or self.picture.get_at((j, i-1)) != colour:
                        targetPixels.append((j, i))

        rects = pygame.sprite.Group()
        for coords in targetPixels:
            rects.add(Platform(coords[0], coords[1], 1, 1))

        print(time.time()-start)
        return rects
