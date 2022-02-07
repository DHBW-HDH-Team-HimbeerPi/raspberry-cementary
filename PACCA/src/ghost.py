import random

class Enemy():

    def __init__(self,x,y):
        self.posxy = [x,y]
        self.lastdir = [0]

    def move(self,xy,pixelArray):
        a =10 
        b=10
        c=10
        d=10
        if(xy[0]>self.posxy[0]):
            c=45
        if(xy[0]<self.posxy[0]):
             d=45
        if(xy[1]>self.posxy[1]):
            a=45
        if(xy[1]<self.posxy[1]):
            b=45

        
        match self.lastdir[0]:
            case 1:
                b=0
            case 2:
                a=0
            case 3:
                d=0
            case 4:
                c=0
        dirList = [1, 2, 3, 4]
        moved=False
        dira = random.choices(dirList, weights=(a, b, c, d), k=1)
        dirb = dira[0]
        for x in range(2):
            match dirb:
                case 1:
                    if (self.posxy[1] < 15 and pixelArray[self.posxy[0]][self.posxy[1] + 1][0] == 0):
                        pixelArray[self.posxy[0]][self.posxy[1] + 1][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1] + 1][2] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][2] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[1] += 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                            moved=True
                    else:
                        dirb = self.lastdir
                case 2:
                    if (self.posxy[1] > 0 and pixelArray[self.posxy[0]][self.posxy[1] - 1][0] == 0):
                        pixelArray[self.posxy[0]][self.posxy[1] - 1][2] = 255
                        pixelArray[self.posxy[0]][self.posxy[1] - 1][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][2] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[1] -= 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                            moved=True
                    else:
                        dirb = self.lastdir
                case 3:
                    if (self.posxy[0] < 15 and pixelArray[self.posxy[0] + 1][self.posxy[1]][0] == 0):
                        pixelArray[self.posxy[0] + 1][self.posxy[1]][2] = 255
                        pixelArray[self.posxy[0] + 1][self.posxy[1]][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][2] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[0] += 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                            moved=True
                    else:
                        dirb = self.lastdir
                case 4:
                    if (self.posxy[0] > 0 and pixelArray[self.posxy[0] - 1][self.posxy[1]][0] == 0):
                        pixelArray[self.posxy[0] - 1][self.posxy[1]][2] = 255
                        pixelArray[self.posxy[0] - 1][self.posxy[1]][1] = 255
                        pixelArray[self.posxy[0]][self.posxy[1]][2] = 0
                        pixelArray[self.posxy[0]][self.posxy[1]][1] = 0
                        self.posxy[0] -= 1
                        dirb = 0
                        if(x==0):
                            self.lastdir = dira
                            moved=True
                    else:
                        dirb = self.lastdir
                case _:
                    dirb = self.lastdir
        if (moved==False):
            self.move(xy,pixelArray)
        


