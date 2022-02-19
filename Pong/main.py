from files.ball import Ball
from files.panel import Panel
from output_framework.output_framework import OutputFramework as oF
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode
# from unicornhatsimulator import unicornhathd as uni
from files.comPlayer import aiPlayer
import numpy as np
import time


class Pong:

    def __init__(self):
        self.leftPanel = Panel(1, 0, 0, 255)
        self.rightPanel = Panel(14, 0, 255, 0)
        self.gameBall = Ball()
        self.score = 0
        self.com = aiPlayer()
        self.alive = True
        self.play()

    def setGameItems(self, gameField, gameObject):
        xPosition = int(gameObject.xPosition)
        yPosition = int(gameObject.yPosition)
        size = gameObject.size
        for x in range(size):
            if yPosition < 16:
                gameField[xPosition][int(yPosition) + x][0] = gameObject.r
                gameField[xPosition][int(yPosition) + x][1] = gameObject.g
                gameField[xPosition][int(yPosition) + x][2] = gameObject.b
        return gameField

    def inputToDirection(self, direc: int):
        global direction
        direction = direc

    def play(self):
        rotationTreshold = 0.4
        self.inputToDirection(0)
        try:
            controller = IMUController(TriggerMode.CALL_CHECK)
            controller.register_trigger(self.inputToDirection, {'direc': -1}, controller.mov_y, -rotationTreshold,
                                        ThresholdType.LOWER)

            controller.register_trigger(self.inputToDirection, {'direc': 1}, controller.mov_y, rotationTreshold,
                                        ThresholdType.HIGHER)
        except NameError:
            print("could NOT find controller")

        while self.alive:
            self.ballCheck()
            comMove = self.com.play(self.gameBall.yPosition, self.rightPanel.yPosition)
            if comMove == -1:
                self.rightPanel.moveDown()
            else:
                if comMove == 1:
                    self.rightPanel.moveUp()
            controller.check_triggers()
            self.check()
            gameField = np.full((16, 16, 3), 0)
            gameField = self.setGameItems(gameField, self.leftPanel)
            gameField = self.setGameItems(gameField, self.rightPanel)
            gameField = self.setGameItems(gameField, self.gameBall)

            oF.setWindow(gameField)
            # for x in range(len(gameField)):
            #    for y in range(len(gameField[x])):
            #        uni.set_pixel(x, y, gameField[x][y][0], gameField[x][y][1], gameField[x][y][2])
            # uni.show()
            # time.sleep(self.speed)
        oF.showText("Score: " + str(self.score), 255, 255, 255, 12, 0.02, 0)

    def ballCheck(self):
        if int(self.gameBall.xPosition) < 1 or int(self.gameBall.xPosition) > 14:
            self.alive = False
        else:
            if int(self.gameBall.xPosition) == 1 or int(self.gameBall.xPosition) == 14:
                if int(self.gameBall.xPosition) == 1 and int(self.gameBall.yPosition) >= self.leftPanel.yPosition and int(self.gameBall.yPosition) <= (
                        self.leftPanel.yPosition + self.leftPanel.size - 1):
                    self.gameBall.panelBounce(self.leftPanel)
                    self.score = self.score + 1
                else:
                    if int(self.gameBall.xPosition) == 14 and int(self.gameBall.yPosition) >= self.rightPanel.yPosition and int(self.gameBall.yPosition) <= (
                            self.rightPanel.yPosition + self.rightPanel.size - 1):
                        self.gameBall.panelBounce(self.leftPanel)
                        self.score = self.score + 1
            if int(self.gameBall.yPosition) <= 0 or int(self.gameBall.yPosition) >= 15:
                self.gameBall.bounce()
            self.gameBall.move()

    def check(self):
        global direction
        if (direction > 0):
            self.leftPanel.moveUp()
        elif (direction < 0):
            self.leftPanel.moveDown()
        direction = 0


if __name__ == "__main__":
    Pong()
