def shiftPixels(pixelArray: list):
    for x in range(len(pixelArray)):
        for y in range(1, len(pixelArray[0])):
            if (pixelArray[x][y-1][3] == 0 and pixelArray[x][y][3] == 0):
                pixelArray[x][y-1] = pixelArray[x][y]
    return True