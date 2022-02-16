from .spriteReader import dimensions, readSprite
from .sprites import numberToSprite
from .maps import Maps
from .addObject import add
from .pixel import setClearPixel

class Map:

    def __init__(self, pixelArray):
        self.map = readSprite(Maps.mario.value, True)
        self.length = int(len(self.map[0])/4)*16
        self.movedPixels = 16
        self.pixelArray = pixelArray
        self.initialMap()

    def addMapToPixelArray(self, pixelArray, start, end):
        grid = 4 #4x4 grid
        for x in range(grid): 
            for y in range(start, end):
                if(end > len(self.map[0])):
                    break
                yPos = y
                spriteNumber = int(self.map[x][y])
                if spriteNumber != 0:
                    sprite = numberToSprite(spriteNumber)
                    if(start > grid):
                        yPos -= grid
                    if(yPos > 8):
                        yPos = y-int(8*(self.movedPixels-32)/16)
                    add(pixelArray, dimensions(sprite), x, yPos)

    def initialMap(self):
        self.addMapToPixelArray(self.pixelArray, 0, 4)

    def updateMap(self):
        grid = 4
        pixel = 16
        if self.movedPixels % pixel == 0 and self.movedPixels > 0:
            pos = int(self.movedPixels/pixel)*grid
            self.addMapToPixelArray(self.pixelArray, pos, pos+grid)

    def moveCameraY(self):
        print(self.movedPixels, self.length)
        if self.movedPixels < self.length:
            self.updateMap()
            self.movedPixels += 1
            for y in range(1, len(self.pixelArray[0])):
                for x in range(len(self.pixelArray)):
                    if self.pixelArray[x][y-1][3] != 1 and self.pixelArray[x][y][3] != 1:
                        self.pixelArray[x][y-1] = self.pixelArray[x][y]
                    if y == len(self.pixelArray[0])-1:
                        setClearPixel(self.pixelArray, x, y) 

    





