import numpy as np
from src.frameBuffer import FrameBuffer
from src.player import Player
from src.unicornHead import showUH
from src.input import Directions
from src.pixel import sanatizeArray
from src.input import inputToDirection
from src.map import Map
import time

try: 
    from output_framework.output_framework import OutputFramework       # type: ignore
    from input_framework.imu_controller import IMUController            # type: ignore
    from input_framework.interface import ThresholdType, TriggerMode    # type: ignore
except ImportError:
    print("No import/output framework found!") # shows error if input/output framework was not found

PIXELS = 16
pixelArray = np.full((PIXELS, PIXELS*2, 4), 0)
ROTATION_THRESHOLD = 0.2

def main():

    player = Player(pixelArray)    # create Player
    map = Map(pixelArray)          # create Map
    frameBuffer = FrameBuffer()    # create Frame Buffer erer

    running = True

    try:
        controller = IMUController(TriggerMode.CALL_CHECK)
        controller.register_trigger(inputToDirection, { 'dir' : 1, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer, 'map': map }, controller.mov_x, ROTATION_THRESHOLD, ThresholdType.HIGHER)
        controller.register_trigger(inputToDirection, { 'dir' : 2, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer, 'map': map }, controller.mov_x, -ROTATION_THRESHOLD, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, { 'dir' : 3, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer, 'map': map }, controller.mov_y, -ROTATION_THRESHOLD, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, { 'dir' : 4, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer, 'map': map }, controller.mov_y, ROTATION_THRESHOLD, ThresholdType.HIGHER)
    except NameError:
        print("No controller found!") # shows error if no controller was found

    while running:
        if player.posX == 13: # if posX is 13, the player fell out of the map in x direction
            running = False   # stop running

        frameBuffer.running = False # frameBuffer inital state

        if frameBuffer.length() > 0: # check for frames in frameBuffer
            frameBuffer.running = True 
            frameBuffer.nextFrame(pixelArray) # show next frame in pixelArray

        try:
            OutputFramework.setWindow(sanatizeArray(pixelArray), 180) # sets the window
            if not frameBuffer.running and not player.isJumping:
                controller.check_triggers() # check for player movement
        except NameError:
            showUH(pixelArray, PIXELS) # shows gui on pc for local development
            
        time.sleep(1/24) # 24 frames per second

if __name__ == "__main__":
    main()