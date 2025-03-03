import regex as re
from client import * 
from jetbot import Robot

def main():
    # Initialize the robot
    robot = Robot()

    context = zmq.Context()
    publisher_ip = "10.13.233.237"
    topics = ["teslabot"]
    query = query_listener(context, publisher_ip, topics)

    # Extract the command from the query
    print(f"Received query: {query}")
    
    # Fix the regex pattern - 'forawrd' seems to be misspelled and missing capture groups
    try:
        command = re.search(r"(forward)", query)
        if command == "forward":
            #robot.forward(7.5)
            print(f"Extracted command: {command.group(1)}")
            robot.forward(0.5)
        else:
            print("No command found in query")
    except AttributeError:
        print("Error: Query is None or invalid")

if __name__ == "__main__":
    main()