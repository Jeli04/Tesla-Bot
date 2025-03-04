from movement import Movement 
from jetbot import Robot, Camera


class TeslaBot():
    def __init__(self):
        self.robot = Robot()
        self.speed = 2.0
        controls = Movement(self.robot)

    def execute(self, commands):
        for command in commands:
            if command["action"] == "Move forward":
                self.movement.forward(command["value"])
            elif command["action"] == "Turn left":
                self.movement.tesla_bot.turn_left(command["value"])
            elif command["action"] == "Turn right":
                self.movement.tesla_bot.turn_right(command["value"])
            else:
                print("invalid action")
                break



