from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT = """You are a math tutor . You only answer to the math questions only. If the question in not related to maths just say sorry.
Strictly give output in json format
Examples:
Q:Can You write a python code to translate text?
A:{{
"Solution":"No i here to answer math question only.",
"Math_question":False
}}
Q: Can u explain me a+b whole square?
A:{{
"Solution":"" ",
"Math_question":True
}}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system",
            "content": SYSTEM_PROMPT
         },
        {
            "role": "user",
            "content": "explain log n"
        }
    ]
)

print(response.choices[0].message.content)
