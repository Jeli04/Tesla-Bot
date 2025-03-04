import regex as re
from client import * 
import sys
sys.path.append("/home/jetbot/jetbot")
sys.path.append("/home/jetbot/jetbot/jetbot")
from jetbot import Robot
from agent import TeslaBot


def main():
    # Initialize the robot
    agent = TeslaBot()

    context = zmq.Context()
    publisher_ip = "10.13.234.109" # "10.10.159.66"
    topics = ["teslabot-text"]

    # send image 
    image_publisher(context, topics, agent.camera):

    query = query_listener(context, publisher_ip, topics)   # get the intial query
    complete = False

    print(f"Received query: {query}")

    while complete != True:
        try: 
            agent.execute(query)
            complete = True
            break
        except AttributeError:
            print("Error: Query is None or invalid")

if __name__ == "__main__":
    main()
