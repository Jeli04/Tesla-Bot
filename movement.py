from jetbot import Robot, Camera
import traitlets
import time

class Movement():
    def __init__(self, robot=None):
        assert robot is not None, "Robot instance is required"

        self.robot = robot
        self.speed = 2.0 # assuming the units are in meters

    def forward(self, distance):
        duration = distance / self.speed
        start_time = time.time()
        
        while time.time() - start_time < duration:
            self.robot.forward(self.speed, duration)

        self.robot.stop()

    def turn_left(self, degree):
        for _ in range(10):
            self.robot.left(self.speed)

    def turn_right(self, degree):
        pass

    def stop(self):
        self.robot.stop()

if __name__ == "__main__":
    movement = Movement()
    movement.forward(2.0)
    movement.turn_left()