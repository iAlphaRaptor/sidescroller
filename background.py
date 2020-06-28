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

        ## Gets dictionary of all rows containing pixels of the target colour.
        targetPixels = {}
        for i in range(self.height):
            for j in range(self.width):
                if self.picture.get_at((j, i)) == colour:
                    if i in targetPixels.keys():
                        targetPixels[i].append(j)
                    else:
                        targetPixels[i] = [j]

        ## Sorts dictionary into a 2D list containing lists of pixels in the same rectangle.
        currentLength = 0
        temp = {}
        rowRects = []
        for row in targetPixels.keys():
            if len(targetPixels[row]) != currentLength:
                currentLength = len(targetPixels[row])

                temp[row] = targetPixels[row]
                rowRects.append(temp)
                temp = {}
            else:
                temp[row] = targetPixels[row]
        rowRects.append(temp)

        ## Sorts each list further to differentiate between different rectangles in the same row.
        seperateRects = []
        for row in rowRects:
            moreTemp = []
            for rowID in row.keys():
                pixelList = row[rowID]
                temp = [pixelList[0]]
                for i in range(1, len(pixelList)):
                    if pixelList[i] - pixelList[i-1] != 1:
                        temp.append(pixelList[i-1])
                        temp.append(pixelList[i])
                temp.append(pixelList[-1])
                moreTemp.append([rowID, temp])
            seperateRects.append(moreTemp)

        ## Creates pygame Rect objects from the list of points.
        rects = []
        for listOfRects in seperateRects:
            for rect in listOfRects:
                for i in range(int(len(rect[1]) / 2)):
                    left = rect[1][i*2] + 1
                    top = rect[0]
                    width = rect[1][(i*2)+1] - rect[1][i*2]
                    height = 1

                    rects.append(pygame.Rect(left, top, width, height))

        return rects
