from enum import Enum
from .player import Player

class Directions(Enum):
    up = 4
    down = 3
    left = 2
    right = 1

def inputToDirection(dir, player: Player):
    if dir == Directions.right.value:
        #player.walkRight()
        print("right")
    elif dir == Directions.left.value:
        #player.walkLeft()
        print("left")
    elif dir == Directions.up.value:
        #player.jump()
        print("up")
    else:
        print("down")
