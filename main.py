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
    topics = ["teslabot"]
    query = query_listener(context, publisher_ip, topics)

    # Extract the command from the query
    print(f"Received query: {query}")
    
    # Fix the regex pattern - 'forawrd' seems to be misspelled and missing capture groups
    try:
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
