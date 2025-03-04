from movement import Movement 
from jetbot import Robot, Camera
import time

class TeslaBot():
    def __init__(self):
        self.robot = Robot()
        self.speed = 2.0
        self.controls = Movement(self.robot)
        self.camera = Camera.instance()


    def execute(self, commands):
        for command in commands:
            if command["action"] == "Move forward":
                self.controls.forward(command["value"])
                time.sleep(2)
            elif command["action"] == "Turn left":
                self.controls.tesla_bot.turn_left(command["value"])
                time.sleep(2)
            elif command["action"] == "Turn right":
                self.controls.tesla_bot.turn_right(command["value"])
                time.sleep(2)
            else:
                print("invalid action")
                exit() # TODO change later
            time.sleep(15)


