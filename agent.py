import ollama
import re

# prompt = """
# You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
# Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
# The avaliable function calls are:
# forward(distance), backward(distance), left(distance), right(distance), stop()
# Use only the neccessary ones. Don't give any uneccessary comments.
# """

# prompt = """
# You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
# Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
# The avaliable function calls are:
# forward(distance), backward(distance), diagonal_left(degree), diagonal_left(right), left(distance), right(distance), stop()
# Use only the neccessary ones. Don't give any uneccessary comments. 
# """

# prompt = """
# You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
# Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
# You must be directly facing the objective so turn if neccessary. Be precise. 
# The avaliable function calls are:
# forward(distance), backward(distance), turn_left(degree), turn_right(degree), stop()
# Use only calls you need to get to the objective. Don't give any uneccessary comments. 
# """

#prompt = """
#You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
#Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
#You must be directly facing the objective so turn if neccessary. Be precise. 
#The avaliable function calls are:
#forward(distance), backward(distance), turn_left(degree), turn_right(degree), stop()
#Use only calls you need to get to the objective. 
#"""

prompt = """
You are an AI embedded in a robot car with a camera.
The POV of the image provided is what you are seeing. 
Only give directions on how to get to desired spot from the User. list each step sequentially to get to the desired spot,
make sure to use keywords such as forward, turn right, turn left, followed by a number of how much to move in that direction in meters
"""


pattern = r"(Move forward|Turn right| Turn left)\s+(\d+)"



response = ollama.chat(
    model='llama3.2-vision',
    messages=[
        {
        'role': 'system',
        'content': prompt
        },
        {
        'role': 'user',
        'content': 'Go to the backpack.',
        'images': ['images/test.jpg']
        }
    ],
    options={"temperature": 0.2, "max_tokens": 500},  
)

print(response.message.content)

matches = re.findall(pattern, response.message.content)

commands = [{"action": action, "value": int(value)} for action, value in matches]

print(commands)