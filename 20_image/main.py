from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "Generate caption of given image in a 50 words"},
            {"type": "input_image",
                "image_url": "https://images.pexels.com/photos/35582289/pexels-photo-35582289.jpeg"}
        ]
    }]

)
print("Response:", response.output_text)
