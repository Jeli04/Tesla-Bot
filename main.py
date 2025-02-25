import regex as re
from client import * 

def main():
    context = zmq.Context()
    publisher_ip = "10.13.233.237"
    topics = ["teslabot"]
    query = query_listener(context, publisher_ip, topics)

    # Extract the command from the query
    print(f"Received query: {query}")
    
    # Fix the regex pattern - 'forawrd' seems to be misspelled and missing capture groups
    try:
        command = re.search(r"(forward)", query)
        if command:
            print(f"Extracted command: {command.group(1)}")
        else:
            print("No command found in query")
    except AttributeError:
        print("Error: Query is None or invalid")

if __name__ == "__main__":
    main()