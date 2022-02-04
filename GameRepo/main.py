import subprocess
from output_framework.output_framework import OutputFramework as oF
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode


class gameChooser:

    def __init__(self):
        self.mainPath = "./"
        self.gamePathes = ["FLAPPA", "PACCA", "Pong", "sidescroller", "SnakeGameClaim"]
        self.gameNames = ["Flappy Dot", "Pacman", "Pong", "Sidescroller", "Snake"]
        self.check = 0
        self.initializeInput()
        self.run()

    def inputToDirection(self, direc: int):
        global direction
        direction = direc

    def initializeInput(self):
        rotationTreshold = 1
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

    def run(self):
        currentGame = 0
        while self.check == 0:
            oF.showText(self.gameNames[currentGame], 255, 255, 255, 14, 50, 50)




if __name__ == "__main__":
    gameChooser()