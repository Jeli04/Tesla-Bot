from jetbot import Robot, Camera
import traitlets

class Movement():
    def __init__(self):
        self.robot = Robot()
        self.camera = Camera.instance()
        self.speed = 2.0 # assuming the units are in meters

    def forward(self, distance):
        time = distance / self.speed   
        self.robot.forward(self.speed, time)

    def turn_left(self, distance):
        time = distance / self.speed   
        self.robot.forward(self.speed, time)

if __name__ == "__main__":
    movement = Movement()
    movement.forward(2.0)
    movement.turn_left(1.0)