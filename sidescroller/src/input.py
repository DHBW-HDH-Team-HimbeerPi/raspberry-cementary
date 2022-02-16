from enum import Enum
from .player import Player

class Directions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

def inputToDirection(dir, pixelArray, player: Player):
    if dir == Directions.right.value:
        player.walkRight(pixelArray)
        print("right")
    elif dir == Directions.left.value:
        player.walkLeft(pixelArray)
        print("left")
    elif dir == Directions.up.value:
        player.jump(pixelArray)
        print("up")
    else:
        print("down")
