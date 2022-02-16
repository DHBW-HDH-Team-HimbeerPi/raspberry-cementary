import random

class Coin():
    test
    def __init__(self,pixelArray):
        while(True):
            x = random.randrange(16)
            y = random.randrange(16)
            if(pixelArray[x][y][1]==0):
                self.posxy = [x,y]
                break
            
    def showcoin(self,pixelArray):
        pixelArray[self.posxy[0]][self.posxy[1]][0]=255
        pixelArray[self.posxy[0]][self.posxy[1]][1]=53
        pixelArray[self.posxy[0]][self.posxy[1]][2]=180