import subprocess
from output_framework.output_framework import OutputFramework as oF
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode
from FLAPPA.main import main as flappy
from PACCA import main as pacman
from Pong import main as pong
from sidescroller import main as amogus
from SnakeGameClaim import main as snake
import time

class gameChooser:

    def __init__(self):
        self.mainPath = "./"
        self.gamePathes = ["FLAPPA", "PACCA", "Pong", "sidescroller", "SnakeGameClaim"]
        self.gameNames = ["Flappy Dot", "Pacman", "Pong", "Sidescroller", "Snake"]
        self.check = 0
        self.currentGame = 0
        self.run()

    def inputToDirection(self, direc: int):
        global direction
        direction = direc

    def run(self):
        rotationTreshold = 0.2
        self.inputToDirection(0)
        try:
            controller = IMUController(TriggerMode.CALL_CHECK)
            controller.register_trigger(self.inputToDirection, {'direc': 1}, controller.mov_x, rotationTreshold,
                                        ThresholdType.HIGHER)
            controller.register_trigger(self.inputToDirection, {'direc': 2}, controller.mov_x, -rotationTreshold,
                                        ThresholdType.LOWER)
            controller.register_trigger(self.inputToDirection, {'direc': 3}, controller.mov_y, -rotationTreshold,
                                        ThresholdType.LOWER)

            controller.register_trigger(self.inputToDirection, {'direc': 4}, controller.mov_y, rotationTreshold,
                                        ThresholdType.HIGHER)
        except NameError:
            print("could NOT find controller")
        while True:
            while self.check == 0:
                oF.showText(self.gameNames[self.currentGame], 255, 255, 255, 12, 0.001, 0)
                controller.check_triggers()
                self.checkInput()
                time.sleep(0.5)
            if self.currentGame == 0:
                flappy()
            elif self.currentGame == 1:
                pacman.main()
            elif self.currentGame == 2:
                pong.Pong()
            elif self.currentGame == 3:
                amogus.main()
            elif self.currentGame == 4:
                snake.main()



    def checkInput(self):
        global direction

        if direction == 2:
            self.check = 1
        elif direction == 3:
            if self.currentGame < 4:
                self.currentGame = self.currentGame + 1
        elif direction == 4:
            if self.currentGame > 0:
                self.currentGame = self.currentGame - 1
        print(direction)
        direction = 0


if __name__ == "__main__":
    gameChooser()