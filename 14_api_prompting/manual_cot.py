from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system",
            "content": SYSTEM_PROMPT
         },
        {
            "role": "user",
            "content": "2+3*5/10 "
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "START", "content": "2+3*5/10"},)
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "The user wants to evaluate the mathematical expression '2+3*5/10'. I need to apply the order of operations (BODMAS/PEMDAS) to solve it."})
        },
    ]
)

print(response.choices[0].message.content)
