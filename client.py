import zmq
import cv2
import numpy as np

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

def image_listener(context, publisher_ip, topics):
    socket = context.socket(zmq.SUB) 
    socket.connect(f"tcp://{publisher_ip}:5555")

    # subscribe to all the topics
    for topic in topics:
        socket.setsockopt_string(zmq.SUBSCRIBE, topic)

    print(f"Subscriber started, listening to {topics}...")

    # Recieve and deocde the image 
    try:
        while True:
            image_bytes = socket.recv_string()  # Receive message
            image_np = np.frombuffer(image_bytes, dtype=np.uint8)
            image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
            cv2.imshow("image", image)
            cv2.waitKey(1)
            break
    except KeyboardInterrupt:
        print("\nSubscriber stopped.")
        socket.close()
        context.term()


if __name__ == "__main__":
    context = zmq.Context()
    publisher_ip = "10.10.159.64"  
    # query_listener(context, publisher_ip, ["teslabot-text", "teslabot-image"])
    image_listener(context, publisher_ip, ["teslabot-image"])

