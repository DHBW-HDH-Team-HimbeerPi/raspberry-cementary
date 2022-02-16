from enum import Enum

from .frameBuffer import FrameBuffer
from .player import Player

#ebjekbjf
class Directions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

def inputToDirection(dir, pixelArray, player: Player, frameBuffer: FrameBuffer):
    print(dir)
    if dir == Directions.right.value:
        player.walkRight(pixelArray)
        print("right")
    elif dir == Directions.left.value:
        player.walkLeft(pixelArray)
        print("left")
    elif dir == Directions.up.value:
        player.jump(pixelArray, frameBuffer)
        print("up")
    else:
        print("down")
