import pygame
from rainbow import colours
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
        Returns list of pygame Rect objects.
        Colour should be given as a 4 number tuple with alpha included."""

        ## Gets dictionary of all rows containing pixels of the target colour
        targetPixels = {}
        for i in range(self.height):
            for j in range(self.width):
                if self.picture.get_at((j, i)) == colour:
                    if i in targetPixels.keys():
                        targetPixels[i].append(j)
                    else:
                        targetPixels[i] = [j]

        currentLength = 0
        temp = {}
        seperateRects = []
        for row in targetPixels.keys():
            if len(targetPixels[row]) != currentLength:
                currentLength = len(targetPixels[row])

                temp[row] = targetPixels[row]
                seperateRects.append(temp)
                temp = {}
            else:
                temp[row] = targetPixels[row]
        seperateRects.append(temp)

        rects = []
        for rect in seperateRects:
            left = list(rect.keys())[0]
            top = rect[list(rect.keys())[0]][0]
            width = list(rect.keys())[-1] - left
            height = rect[list(rect.keys())[-1]][-1] - top

            rects.append(pygame.Rect(left, top, width, height))

        return rects
