def add(pixelArray: list, addArray: list, outOfView):
    pixel = len(pixelArray)
    for x in range(pixel):
        for y in range(pixel):
            if addArray[x][y][0] != 0 or addArray[x][y][1] != 0 or addArray[x][y][2] != 0:
                morePixels = 0
                if outOfView:
                    morePixels = pixel
                pixelArray[x][morePixels+y] = addArray[x][y]