from openai import OpenAI
from dotenv import load_dotenv
import os
import json


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPEN_AI_KEY")
)


SYSTEM_PROMPT = """You are an expert ai assistant.You work on chain on thoughts. You work START ,PLAN and OUTPUT steps.
You need to first PLAN whats need to done.The plan can be of multiple steps.
Once you think enough give the OUTPUT.
Rules:
-Strictly follow the json output format.
-only one step at a time
-The sequence of steps is start (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT(which is going todislay on the user).


output JSON format:
{"step:"START"| "PLAN"|"OUTPUT, "content":"string"}

Example:
START : Hey can you solve 2+3 * 5/10
PLAN:{"step":"PLAN","content":"Seems lik user is interested in math problem"  }
PLAN:{"step":"PLAN","content":"Looks like problem can be solved using BODMAS method"  }
PLAN:{"step":"PLAN","content":"Yes the  problem can be solved using BODMAS method"  }

PLAN:{"step":"PLAN","content":"First we mutlipy 3 *5 which give 15"  }

PLAN:{"step":"PLAN","content":"Then we divide 15 which give 10 which give 1.5"  }

PLAN:{"step":"PLAN","content":"Then we add 1.5 with 2 give 3.5"  }

OUTPUT:{"step":"OUTPUT","content":"3.5"  }


"""


messageHistory = [
    {"role": "system", "content": SYSTEM_PROMPT},
]
user_query = input("👉")
messageHistory.append({"role": "user", "content": user_query})
while True:

    response = client.chat.completions.create(
        model="gpt-5-nano-2025-08-07",
        response_format={"type": "json_object"},

        messages=messageHistory)

    raw_data = response.choices[0].message.content
    pasrsed_data = json.loads(raw_data)
    messageHistory.append({
        "role": "assistant",
        "content": raw_data   # MUST be string
    })
    state = pasrsed_data["step"]
    if state == "START":
        print(f"🔥 {raw_data}")
        continue
    if state == "PLAN":
        print(f"🧠 {raw_data}")
        continue
    if state == "OUTPUT":
        print(f"💪 {raw_data}")
        break
