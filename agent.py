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

# prompt = """
# You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
# Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
# You must be directly facing the objective so turn if neccessary. Be precise. 
# The avaliable function calls are:
# forward(distance), backward(distance), turn_left(degree), turn_right(degree), stop()
# Use only calls you need to get to the objective. Don't give any uneccessary comments. 
# """

prompt = """
You are an AI embedded in a robot car with a camera. You are given text instructions and an image.
Output the function calls to control the robot based on the prompt. The POV of the image is what you are seeing. 
You must be directly facing the objective so turn if neccessary. Be precise. 
The avaliable function calls are:
forward(distance), backward(distance), turn_left(degree), turn_right(degree), stop()
Use only calls you need to get to the objective. Keep the units in meters.
"""

# response = ollama.chat(
#     model='llama3.2-vision',
#     messages=[
#         {
#         'role': 'system',
#         'content': prompt
#         },
#         {
#         'role': 'user',
#         'content': 'Go to the TV.',
#         'images': ['images/test2.jpg']
#         }
#     ],
#     options={"temperature": 0.2, "max_tokens": 500},  
# )

# print(response)



from openai import OpenAI
import base64
client = OpenAI()

# Convert image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Path to your local image
image_path = "images/test2.jpg"  # Change this to your image file path
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4.5-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])