import regex as re
from client import * 
import sys
sys.path.append("/home/jetbot/jetbot")
sys.path.append("/home/jetbot/jetbot/jetbot")
from jetbot import Robot
from movement import Movement

def main():
    # Initialize the robot
    robot = Robot()
    movement = Movement(robot)

    context = zmq.Context()
    publisher_ip = "10.10.159.66"
    topics = ["teslabot-text"]
    query = query_listener(context, publisher_ip, topics)   # get the intial query
    complete = False

    print(f"Received query: {query}")

    while complete != True:
        try: 
            # TODO feed to the Agent and get the parsed functions 
            commands = []

            for command in commands:
                action = command['action']
                value = command['value']

                if action == "forward":
                    movement.forward(value)
                elif action == "turn_left":
                    movement.turn_left(value)
                elif action == "turn_right":
                    movement.turn_right(value)
                else:
                    print("Invalid action")
                    break
        except AttributeError:
            print("Error: Query is None or invalid")

if __name__ == "__main__":
    main()