def add(pixelArray: list, addArray: list):
    for x in range(len(pixelArray)):
        for y in range(len(pixelArray[0])):
            if addArray[x][y][0] != 0 or addArray[x][y][1] != 0 or addArray[x][y][3] != 0:
                pixelArray[x][y] = addArray[x][y]
    