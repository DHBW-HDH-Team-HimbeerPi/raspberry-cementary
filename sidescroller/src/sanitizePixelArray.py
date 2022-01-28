import numpy as np

def sanatizeArray(pixelArray):
    newPixelArray = np.full((16, 16, 4), 0)
    for x in range(0, len(pixelArray[0])):
        for y in range(1, len(pixelArray[0])):
            newPixelArray[x][y] = pixelArray
    return newPixelArray