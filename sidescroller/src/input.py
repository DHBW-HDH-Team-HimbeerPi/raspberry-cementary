from enum import Enum

from .frameBuffer import FrameBuffer
from .player import Player

#ebjewgw
class Directions(Enum):
    up = 4
    down = 3
    left = 1
    right = 2

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
