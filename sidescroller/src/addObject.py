def add(pixelArray: list, addArray: list, pixels):
    for x in range(pixels):
        for y in range(pixels):
            if addArray[x][y][0] != 0 or addArray[x][y][1] != 0 or addArray[x][y][3] != 0:
                pixelArray[x][y] = addArray[x][y]

def addOutOfBounds(pixelArray: list, addArray: list, pixels):
    for x in range(pixels, pixels*2):
        for y in range(0, pixels):
            if addArray[x][y][0] != 0 or addArray[x][y][1] != 0 or addArray[x][y][3] != 0:
                pixelArray[x][y] = addArray[x][y]
    