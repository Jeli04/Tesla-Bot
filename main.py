import regex as re
from client import * 
import sys
sys.path.append("/home/jetbot/jetbot")
sys.path.append("/home/jetbot/jetbot/jetbot")
from jetbot import Robot


def main():
    # Initialize the robot
    robot = Robot()

    context = zmq.Context()
    publisher_ip = "10.10.159.66"
    topics = ["teslabot-text"]
    query = query_listener(context, publisher_ip, topics)

    print(f"Received query: {query}")
    
    try:
        # TODO - Replace this with the parser to get a list of commands to execute
        command = re.search(r"(forward)", query)
        if command:
            print(f"Extracted command: {command.group(1)}")
            for i in range(100000):
                #robot.forward(7.5)
                robot.set_motors(0.6, 0.6)
        else:
            print("No command found in query")
    except AttributeError:
        print("Error: Query is None or invalid")

if __name__ == "__main__":
    main()
