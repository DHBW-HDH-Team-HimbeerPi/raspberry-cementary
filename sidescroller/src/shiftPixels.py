
def shiftPixelsY(pixelArray: list):
    for x in range(len(pixelArray)):
        for y in range(1, len(pixelArray[0])):
            if (pixelArray[x][y-1][3] != 1 and pixelArray[x][y][3] != 1):
                pixelArray[x][y-1] = pixelArray[x][y]
    return True

def shiftPlayerUp(pixelArray: list):
    for x in range(0, len(pixelArray[0])):
        for y in range(1, len(pixelArray[0])):
            if (pixelArray[x][y][3] == 1):
                pixelArray[x-1][y] = pixelArray[x][y]
                pixelArray[x][y][0] = 0  
                pixelArray[x][y][1] = 0  
                pixelArray[x][y][2] = 0  
                pixelArray[x][y][3] = 0  

def shiftPlayerDown(pixelArray: list):
    border = False
    for x in range(0, len(pixelArray[0])):
        for y in range(0, len(pixelArray[0])):
            x16 = 15-x
            if (pixelArray[x16][y][3] == 1):
                if(x16 == 15):
                    border = True
                    break
                pixelArray[x16+1][y] = pixelArray[x16][y]
                pixelArray[x16][y][0] = 0  
                pixelArray[x16][y][1] = 0  
                pixelArray[x16][y][2] = 0  
                pixelArray[x16][y][3] = 0 
        if(border):
            break

#def walkRight(pixelArray: list):


                