import zmq

def query_listener(context, publisher_ip, topics):
    socket = context.socket(zmq.SUB)  # Create a subscriber socket

    # Connect to the publisher
    socket.connect(f"tcp://{publisher_ip}:5555")

    for topic in topics:
        socket.setsockopt_string(zmq.SUBSCRIBE, topic)  # Subscribe to a topic
    

    print(f"Subscriber started, listening to {topics}...")

    try:
        while True:
            message = socket.recv_string()  # Receive message
            print(f"Received: {message}")
            return message
    except KeyboardInterrupt:
        print("\nSubscriber stopped.")
        socket.close()
        context.term()


if __name__ == "__main__":
    context = zmq.Context()
    publisher_ip = "10.13.233.237"  # Replace with your Jetson Nano's IP address
    query_listener(context, publisher_ip, ["teslabot"])