from numpy import pi


def add(pixelArray: list, addArray: list):
    for x in range(len(pixelArray)):
        for y in range(len(pixelArray[0])):
            pixelArray[x][y] = addArray[x][y]
    