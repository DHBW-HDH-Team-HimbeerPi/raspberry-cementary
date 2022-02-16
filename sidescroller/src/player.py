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
        add(pixelArray, self.dimensions(), 3, 0)

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
                        self.posX = 16-x*3
                        self.posY = y
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

    def walkRight(self, pixelArray):
        #check if walking right is possible
        if self.posY < 14: 
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

    def walkLeft(self, pixelArray):
        #check if walking left is possible
        if self.posY > 2:
            self.posY -= 1
            self.updateVelocity(2)
            self.lastWalkDirection = 2 # 1=right/2=left
            rng = len(pixelArray)
            for x in range(rng):
                for y in range(rng):
                    if (pixelArray[x][y][3] == 1):
                        pixelArray[x][y-1] = pixelArray[x][y]
                        setClearPixel(pixelArray, x, y)

    def shiftPlayerUp(self, pixelArray):
        #check if going up is possible
        if self.posX > 2:
            rng = len(pixelArray)
            self.posX -= 1
            for x in range(rng):
                for y in range(1, rng):
                    if (pixelArray[x][y][3] == 1 and x > 0):
                        pixelArray[x-1][y] = pixelArray[x][y]
                        setClearPixel(pixelArray, x, y)  

    def shiftPlayerDown(self, pixelArray):
        #check if going down is possible
        if self.posX < 13:
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
                    self.shiftPlayerUp(pixelArrayCopy)
                changed = True
            elif oldJumpPosY > jumpPosY:
                for jmps in range(oldJumpPosY-jumpPosY):
                    self.shiftPlayerDown(pixelArrayCopy)
                changed = True
                
            if changed:
                frameBuffer.addFrame(pixelArrayCopy)

            x += 1

        self.isJumping = False