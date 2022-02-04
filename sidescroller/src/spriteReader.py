from pathlib import Path
import csv
import numpy as np
import random as rand
import math

def readSprite(fileName, readMap):
    basePath = Path(__file__).parent
    if(readMap):
        filePath = (basePath / ("../maps/"+fileName)).resolve()
    else:
        filePath = (basePath / ("../sprites/"+fileName)).resolve()
    

    with open(filePath) as file:
        sprite = [line for line in csv.reader(file)]
        return sprite

def setPixelColor(pixelArray, x, y, colorR, colorG, colorB):
    pixelArray[x][y][0] = colorR
    pixelArray[x][y][1] = colorG
    pixelArray[x][y][2] = colorB
    pixelArray[x][y][3] = 2

def setRandomPixelColor(pixelArray, x, y):
    pixelArray[x][y][0] = rand.randrange(100, 255)
    pixelArray[x][y][1] = rand.randrange(100, 255)
    pixelArray[x][y][2] = rand.randrange(100, 255)
    pixelArray[x][y][3] = 2

def dimensions(fileName, quadrant):
    pixels = 16
    x = math.floor(quadrant/4)
    y = quadrant % 4
    sprite = readSprite(fileName, False)
    pixelArray = np.full((pixels, pixels, 4), 0)
    for x in range(pixels):
        for y in range(pixels):
            if(int(sprite[x][y]) != 0):
                pixelArray[x][y] = int(sprite[x][y])
                setRandomPixelColor(pixelArray, x, y)
    return pixelArray