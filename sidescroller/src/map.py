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
                    if start > grid:
                        yPos -= grid
                    
                    if yPos > 7:
                        yPos = yPos-8
                        if self.movedPixels % 32 == 0:
                            yPos = int(yPos-4*(self.movedPixels/32))
                        else:
                            yPos = int(yPos-4*(self.movedPixels-16)/32)
                        #yPos = y-int(8*(self.movedPixels-32)/16)
                        #if yPos == 0:
                        #    yPos += grid
                        print("yPos after: ", yPos)

                    print("add: ", x, yPos, " moved pixels: ", self.movedPixels)
                    add(pixelArray, dimensions(sprite), x, yPos)

    def initialMap(self):
        self.addMapToPixelArray(self.pixelArray, 0, 4)

    def updateMap(self, pixelArray):
        grid = 4
        pixel = 16
        if self.movedPixels % pixel == 0 and self.movedPixels > 0:
            pos = int(self.movedPixels/pixel)*grid
            self.addMapToPixelArray(pixelArray, pos, pos+4)

    def moveCameraY(self, pixelArray):
        #print(self.movedPixels, self.length)
        if self.movedPixels < self.length+8:
            self.updateMap(pixelArray)
            self.movedPixels += 1
            for y in range(1, len(pixelArray[0])):
                for x in range(len(pixelArray)):
                    if pixelArray[x][y-1][3] != 1 and pixelArray[x][y][3] != 1:
                        pixelArray[x][y-1] = pixelArray[x][y]
                    if y == len(pixelArray[0])-1:
                        setClearPixel(pixelArray, x, y) 

    





