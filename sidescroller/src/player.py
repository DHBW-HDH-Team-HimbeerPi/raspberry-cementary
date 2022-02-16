import numpy as np
import random
import math

from .frameBuffer import FrameBuffer
from .spriteReader import readSprite, setPixelColor
from .sprites import Sprites
from .addObject import add
from .pixel import setPixelColor, setClearPixel

class Player():

    def __init__(self, pixelArray):
        self.amogus = readSprite(Sprites.player.value, False)
        self.colorR = random.randrange(100, 255)
        self.colorG = random.randrange(100, 255)
        self.colorB = random.randrange(100, 255)
        self.posX = 0
        self.posY = 0
        self.jumpHeight = 4
        self.velocity = 1
        self.lastWalkDirection = 0
        self.isJumping = False
        self.positioningX = 2
        self.positioningY = 0
        add(pixelArray, self.dimensions(), self.positioningX, self.positioningY)

    def setPixelColorSelf(self, pixelArray, x, y):
        setPixelColor(pixelArray, x, y, self.colorR, self.colorG, self.colorB, 1)

    def dimensions(self):
        pixelArray = np.full((len(self.amogus), len(self.amogus[0]), 4), 0)
        for x in range(len(pixelArray)):
            for y in range(len(pixelArray[0])):
                if int(self.amogus[x][y]) != 0:
                    pixelArray[x][y] = int(self.amogus[x][y])
                    if int(self.amogus[x][y]) == 2:
                        setPixelColor(pixelArray, x, y, 0, 100, 255, 1)
                        self.posX = (4*self.positioningX+y)-1
                        self.posY = (4*self.positioningY+x)+1
                    else:
                        self.setPixelColorSelf(pixelArray, x, y)
        return pixelArray

    def updateVelocity(self, walkDirection):
        lwd = self.lastWalkDirection
        if self.velocity < 5 and not self.isJumping:
            if lwd == walkDirection or lwd == 0:
                self.velocity +=1
            else:
                self.velocity = 1

    def walkingRightPossible(self, pixelArray):
        if pixelArray[self.posX+2][self.posY+2][3] == 0 and pixelArray[self.posX+1][self.posY+2][3] == 0 and pixelArray[self.posX][self.posY+2][3] == 0 and pixelArray[self.posX-1][self.posY+1][3] == 0:
            return True
        else:
            return False

    def walkRight(self, pixelArray):
        #check if walking right is possible
        if self.posY < 7:
            if self.walkingRightPossible(pixelArray): 
                self.posY += 1
                self.updateVelocity(1)
                self.lastWalkDirection = 1 # 1=right/2=left
                rng = len(pixelArray)
                for x in range(rng):
                    for y in range(rng):
                        y16 = 15-y
                        if (pixelArray[x][y16][3] == 1):
                            pixelArray[x][y16+1] = pixelArray[x][y16]
                            setClearPixel(pixelArray, x, y16)

    def walkingLeftPossible(self, pixelArray):
        if pixelArray[self.posX+2][self.posY-2][3] == 0 and pixelArray[self.posX+1][self.posY-2][3] == 0 and pixelArray[self.posX][self.posY-2][3] == 0 and pixelArray[self.posX-1][self.posY-1][3] == 0:
            return True
        else:
            return False

    def walkLeft(self, pixelArray):
        print(self.posX, self.posY)
        #check if walking left is possible
        if self.posY > 2:
            if self.walkingLeftPossible(pixelArray):
                self.posY -= 1
                self.updateVelocity(2)
                self.lastWalkDirection = 2 # 1=right/2=left
                rng = len(pixelArray)
                for x in range(rng):
                    for y in range(rng):
                        if (pixelArray[x][y][3] == 1):
                            pixelArray[x][y-1] = pixelArray[x][y]
                            setClearPixel(pixelArray, x, y)

    def goingUpPossible(self, pixelArray):
        if self.posX-2 > 0:
            if pixelArray[self.posX-2][self.posY][3] == 0 and pixelArray[self.posX-2][self.posY-1][3] == 0 and pixelArray[self.posX-2][self.posY+1][3] == 0:
                return True
        else:
            return False

    def shiftPlayerUp(self, pixelArray):
        #check if going up is possible
        if self.goingUpPossible(pixelArray):
            rng = len(pixelArray)
            self.posX -= 1
            for x in range(rng):
                for y in range(1, rng):
                    if (pixelArray[x][y][3] == 1 and x > 0):
                        pixelArray[x-1][y] = pixelArray[x][y]
                        setClearPixel(pixelArray, x, y)  

    def goingDownPossible(self, pixelArray):
        if self.posX+3<16:
            if pixelArray[self.posX+3][self.posY][3] == 0 and pixelArray[self.posX+3][self.posY-1][3] == 0 and pixelArray[self.posX+3][self.posY+1][3] == 0:
                return True
        else:
            print("down false")
            return False

    def shiftPlayerDown(self, pixelArray):
        #check if going down is possible
        if self.goingDownPossible(pixelArray):
            rng = len(pixelArray)
            self.posX += 1
            for x in range(rng):
                for y in range(rng):
                    x16 = 15-x
                    if (pixelArray[x16][y][3] == 1 and x16 < rng-1):
                        pixelArray[x16+1][y] = pixelArray[x16][y]
                        setClearPixel(pixelArray, x16, y)

    def jumpFunc(self, x):
        velocity = (self.velocity**-1)+0.3
        if self.velocity == 1:
            velocity = 1
        return round((-((x*velocity)-math.sqrt(self.jumpHeight))**2)+self.jumpHeight)

    def jump(self, pixelArray: list, frameBuffer: FrameBuffer):
        self.isJumping = True
        jumpPosX = 0
        jumpPosY = 0
        oldJumpPosX = jumpPosX
        oldJumpPosY = jumpPosY
        pixelArrayCopy = pixelArray.copy()
        jumpsUp = 0
        jumpsDown = 0
        x = 0
        
        while self.jumpFunc(x) >= 0:
            y = self.jumpFunc(x)
            changed = False
            oldJumpPosY = jumpPosY
            oldJumpPosX = jumpPosX
            jumpPosX = x
            jumpPosY = y


            if oldJumpPosX != jumpPosX:
                self.walkRight(pixelArrayCopy)
                changed = True
            if oldJumpPosY < jumpPosY:
                for jmps in range(jumpPosY-oldJumpPosY):
                    jumpsUp += 1
                    self.shiftPlayerUp(pixelArrayCopy)
                changed = True
            elif oldJumpPosY > jumpPosY:
                for jmps in range(oldJumpPosY-jumpPosY):
                    jumpsDown += 1
                    self.shiftPlayerDown(pixelArrayCopy)
                changed = True
                
            if changed:
                frameBuffer.addFrame(pixelArrayCopy)

            x += 1

        if jumpsDown < jumpsUp:
            for jmps in range(jumpsUp-jumpsDown):
                self.shiftPlayerDown(pixelArrayCopy)
                frameBuffer.addFrame(pixelArrayCopy)

        self.isJumping = False