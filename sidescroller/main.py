import time
import numpy as np
from src.shiftPixels import shiftPlayerDown, shiftPlayerUp, shiftPixelsY
from src.addObject import add
from src.player import Player
from src.unicornHead import showUH
from src.spriteReader import dimensions
from src.sprites import Sprites
#from output_framework.output_framework import OutputFramework
#from input_framework.imu_controller import IMUController
#from input_framework.interface import ThresholdType, TriggerMode

PIXELS = 16
pixelArray = np.full((PIXELS, PIXELS*2, 4), 0)
pixelArray[10][10][0] = 255
#ctrl = IMUController(TriggerMode.CALL_CHECK)
#ctrl.register_trigger(movePlayerRight, {'velocity' : 1 }, ctrl.mov_y, 0.3, ThresholdType.HIGHER)

def main():

    joe = Player()
    add(pixelArray, joe.dimensions(), False)
    add(pixelArray, dimensions(Sprites.mapStairs.value), True)
    add(pixelArray, dimensions(Sprites.mapPlatform.value), True)
    #show(pixelArray)
    running = True
    times = 0

    while running:
        #events/input:
        #ctrl.check_triggers()
        #update:
        showUH(pixelArray, PIXELS)
        running = shiftPixelsY(pixelArray)
        #draw:
        #OutputFramework.setWindow(pixelArray)
        time.sleep(0.25)  #24 fps

if __name__ == "__main__":
    main()