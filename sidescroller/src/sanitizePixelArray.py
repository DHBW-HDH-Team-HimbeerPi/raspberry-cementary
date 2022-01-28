import numpy as np

def sanatizeArray(pixelArray):
    newPixelArray = np.full((16, 16, 4), 0)
    rng = len(newPixelArray[0])
    for x in range(rng):
        for y in range(rng):
            newPixelArray[x][y] = pixelArray[x][y]
    return newPixelArray