from PIL import Image
import numpy as np
from pathlib import Path



def createLevel(pixelArray,number):
    level = "Level"+str(number)+".png"
    basePath = Path(__file__).parent
    filePath = (basePath / (level)).resolve()
    img = Image.open(filePath).convert('L')

    np_img = np.array(img)
    np_img = ~np_img  # invert B&W
    np_img[np_img > 0] = 1
    for x in range(16):
        for y in range(16):
            if (np_img[x][y] == 1):
                pixelArray[x][y][0] = 91
                pixelArray[x][y][1] = 58
                pixelArray[x][y][2] = 41
    return pixelArray

def checkalive(Joe,ENEMIES):
    for obj in ENEMIES:
        if(obj.posxy[0]==Joe.posxy[0] and obj.posxy[1]==Joe.posxy[1]):
            return False
        
    return True
def checkcoin(Joe,Coin):
    if (Joe.posxy[0]==Coin.posxy[0] and Joe.posxy[1]==Coin.posxy[1]):
        
        return True
    return False
        