import time
from xml.etree.ElementTree import PI
import numpy as np
from src.shiftPixels import shiftPixels
from src.addObject import add
from src.player import Player
from src.spriterReader import readSprite

from unicorn_hat_sim import unicornhathd as uh
#from output_framework.output_framework import OutputFramework

PIXELS = 16
pixelArray = np.full((PIXELS , PIXELS, 4), 0)
pixelArray[10][10][0] = 255

def main():

    joe = Player(PIXELS)
    add(pixelArray, joe.dimensions())
    #show(pixelArray)
    running = True

    amogus = readSprite("amogus.csv")
    print(amogus)
    uh.rotation(270)

    while running:
        #events
        #input
        #update
        running = shiftPixels(pixelArray)
        #draw
        uh.clear()
        for i in range(0, PIXELS):
            for j in range(0, PIXELS):
                uh.set_pixel(i, j, pixelArray[i][j][0],  pixelArray[i][j][1],  pixelArray[i][j][2])
        uh.show()
        #OutputFramework.setWindow(pixelArray)
        time.sleep(0.5) 

if __name__ == "__main__":
    main()
        





