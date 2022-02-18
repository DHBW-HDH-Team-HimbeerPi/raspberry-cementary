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
    from output_framework.output_framework import OutputFramework # type: ignore
    from input_framework.imu_controller import IMUController # type: ignore
    from input_framework.interface import ThresholdType, TriggerMode # type: ignore
except ImportError:
    print("No imports found!")

PIXELS = 16
pixelArray = np.full((PIXELS, PIXELS*2, 4), 0)

def main():

    player = Player(pixelArray)    # create Player
    map = Map(pixelArray)          # create Map
    frameBuffer = FrameBuffer()    # create Frame Buffer erer

    running = True

    try:
        rotationTreshold = 0.35
        controller = IMUController(TriggerMode.CALL_CHECK)
        controller.register_trigger(inputToDirection, { 'dir' : 1, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_x, rotationTreshold, ThresholdType.HIGHER)
        controller.register_trigger(inputToDirection, { 'dir' : 2, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_x, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, { 'dir' : 3, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_y, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, { 'dir' : 4, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_y, rotationTreshold, ThresholdType.HIGHER)
    except NameError:
        print("No controller found!")

    while running:
        bufferRunning = False

        if frameBuffer.length() > 0:
            bufferRunning = True
            frameBuffer.nextFrame(pixelArray)

        try:
            OutputFramework.setWindow(sanatizeArray(pixelArray), 180)
            if not bufferRunning and not player.isJumping:
                controller.check_triggers()
        except NameError:
            showUH(pixelArray, PIXELS)
                
        inputToDirection(2, pixelArray, player, frameBuffer, map)
        time.sleep(1/2)

if __name__ == "__main__":
    main()