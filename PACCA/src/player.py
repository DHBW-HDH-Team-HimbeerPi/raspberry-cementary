

class Player():

    def __init__(self,x,y):
        self.posxy = [x,y]
        self.lastdir =0



    def getpos():
        return self.posxy
    def move(self,dira,pixelArray):

        dirb = dira
        for x in range(2):
            match dirb:
                if(dirb==1):
                    if (self.posxy[1] < 15 and pixelArray[self.posxy[0]][self.posxy[1] + 1][0] != 91):
                        pixelArray[self.posxy[0]][self.posxy[1] + 1][0] = 255
                        pixelArray[self.posxy[0]][self.posxy[1] + 1][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][0] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[1] += 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                    else:
                        dirb = self.lastdir
                elif(dirb==2):
                    if (self.posxy[1] > 0 and pixelArray[self.posxy[0]][self.posxy[1] - 1][0] != 91):
                        pixelArray[self.posxy[0]][self.posxy[1] - 1][0] = 255
                        pixelArray[self.posxy[0]][self.posxy[1] - 1][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][0] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[1] -= 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                    else:
                        dirb = self.lastdir
                elif(dirb==3):
                    if (self.posxy[0] < 15 and pixelArray[self.posxy[0] + 1][self.posxy[1]][0] != 91):
                        pixelArray[self.posxy[0] + 1][self.posxy[1]][0] = 255
                        pixelArray[self.posxy[0] + 1][self.posxy[1]][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][0] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[0] += 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                    else:
                        dirb = self.lastdir
                elif(dirb==4):
                    if (self.posxy[0] > 0 and pixelArray[self.posxy[0] - 1][self.posxy[1]][0] != 91):
                        pixelArray[self.posxy[0] - 1][self.posxy[1]][0] = 255
                        pixelArray[self.posxy[0] - 1][self.posxy[1]][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][0] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[0] -= 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                    else:
                        dirb = self.lastdir
                else:
                    dirb = self.lastdir


