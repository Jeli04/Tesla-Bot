import zmq
import cv2
import numpy as np
import ipywidgets.widgets as widgets
from jetbot import Camera
from jetbot import bgr8_to_jpeg
import traitlets

camera = Camera.instance()

# Setup ZMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.PUB)  # Or zmq.PUSH for a simple pipeline
socket.bind("tcp://*:5555")
topics = ["teslabot-image"]

print("Publishing starting...")

image = widgets.Image(format='jpeg', width=300, height=300)
camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)

# Read image and encode
image_bytes = image.value
socket.send(image_bytes)  # Send as bytes