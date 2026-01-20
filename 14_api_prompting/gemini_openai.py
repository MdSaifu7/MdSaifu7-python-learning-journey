from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
   
        {
            "role": "user",
            "content": "Explain me about LLM"
        }
    ]
)

print(response.choices[0].message.content)
