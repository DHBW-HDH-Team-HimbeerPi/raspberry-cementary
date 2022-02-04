from pathlib import Path
import csv
import numpy as np
import random as rand

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

def dimensions(fileName):
    sprite = readSprite(fileName, False)
    pixelArray = np.full((16 , 16, 4), 0)
    for x in range(0, len(pixelArray)):
        for y in range(0, len(pixelArray[0])):
            if(int(sprite[x][y]) != 0):
                pixelArray[x][y] = int(sprite[x][y])
                setRandomPixelColor(pixelArray, x, y)
    return pixelArray