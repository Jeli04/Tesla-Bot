import ollama

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

prompt = """
You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
You must be directly facing the objective, turn if neccessary. Be precise. 
The avaliable function calls are:
forward(distance), backward(distance), turn_left(degree), turn_right(degree), stop()
Use only the neccessary ones. Don't give any uneccessary comments. 
"""

response = ollama.chat(
    model='llama3.2-vision',
    messages=[
        {
        'role': 'system',
        'content': prompt
        },
        {
        'role': 'user',
        'content': 'Go to the TV.',
        'images': ['images/test.jpg']
        }
    ],
    options={"temperature": 0.1, "max_tokens": 200},  
)

print(response)