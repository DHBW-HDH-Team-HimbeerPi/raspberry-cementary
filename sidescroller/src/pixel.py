import numpy as np

def setPixelColor(pixelArray, x, y, r, g, b, pixelValue):
    pixelArray[x][y][0] = r
    pixelArray[x][y][1] = g
    pixelArray[x][y][2] = b
    pixelArray[x][y][3] = 1

def setClearPixel(pixelArray, x, y):
    setPixelColor(pixelArray, x, y, 0, 0, 0, 0)

def sanatizeArray(pixelArray):
    newPixelArray = np.full((16, 16, 4), 0)
    rng = len(newPixelArray[0])
    for x in range(rng):
        for y in range(rng):
            newPixelArray[x][y] = pixelArray[x][y]
    return newPixelArray