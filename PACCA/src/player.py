

class Player():

    def __init__():
        self.posxy = (0,0)
        self.lastdir =(0)

    def move(dira,pixelArray):

        dirb = dira
        for x in range(2):
            match dirb:
                case 1:
                    if (self.posxy[1] < 15 and pixelArray[self.posxy[0]][self.posxy[1] + 1][0] == 0):
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
                case 2:
                    if (self.posxy[1] > 0 and pixelArray[self.posxy[0]][self.posxy[1] - 1][0] == 0):
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
                case 3:
                    if (self.posxy[0] < 15 and pixelArray[self.posxy[0] + 1][self.posxy[1]][0] == 0):
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
                case 4:
                    if (self.posxy[0] > 0 and pixelArray[self.posxy[0] - 1][self.posxy[1]][0] == 0):
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
                case _:
                    dirb = self.lastdir


