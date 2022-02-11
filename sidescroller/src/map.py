from .spriteReader import dimensions, readSprite
from .sprites import numberToSprite
from .maps import Maps
from .addObject import add

class Map:

    def __init__(self, pixelArray):
        self.map = readSprite(Maps.mario.value, True)
        self.length = int(len(self.map[0])/4)*16
        self.movedPixels = 16
        self.initialMap(pixelArray)

    def addMapToPixelArray(self, pixelArray, start, end):
        grids = 4
        for x in range(grids): 
            for y in range(start, end):
                if(end > len(self.map[0])):
                    break
                yPos = y
                spriteNumber = int(self.map[x][y])
                if spriteNumber != 0:
                    sprite = numberToSprite(spriteNumber)
                    if(start > 4):
                        yPos -= 4
                    add(pixelArray, dimensions(sprite), x, yPos)

    def initialMap(self, pixelArray):
        self.addMapToPixelArray(pixelArray, 0, 4)

    def updateMap(self, pixelArray):
        grid = 4
        pixel = 16
        if self.movedPixels % pixel == 0 and self.movedPixels > 0:
            pos = int(self.movedPixels/pixel)*grid
            self.addMapToPixelArray(pixelArray, pos, pos+grid)

    def moveCameraY(self, pixelArray):
        if self.movedPixels < self.length:
            self.updateMap(pixelArray)
            self.movedPixels += 1
            for y in range(1, len(pixelArray[0])):
                for x in range(len(pixelArray)):
                    if pixelArray[x][y-1][3] != 1 and pixelArray[x][y][3] != 1:
                        pixelArray[x][y-1] = pixelArray[x][y]
                    if y == len(pixelArray[0])-1:
                        pixelArray[x][y][0] = 0  
                        pixelArray[x][y][1] = 0  
                        pixelArray[x][y][2] = 0  
                        pixelArray[x][y][3] = 0 

    





