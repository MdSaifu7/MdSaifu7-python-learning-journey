from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests


# add before next request
load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPEN_AI_KEY")
)


SYSTEM_PROMPT = """You are an expert ai assistant.You work on chain on thoughts. You work START ,PLAN and OUTPUT steps.
You need to first PLAN whats need to done.The plan can be of multiple steps.
Once you think enough give the OUTPUT.
You can use the available tools if required.
for every tool call wait for OBSERVE step in which we get the output from the tool
Rules:
-Strictly follow the json output format.
-only one step at a time
-The sequence of steps is start (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT(which is going to dislay on the user).


output JSON format:
{"step:"START"| "PLAN"|"OUTPUT" | "TOOl, "content":"string","tool":"string",
"input":"string"}

Available Tools:
-> get_weather(city: str). takes city name as input form the user and return the output about the weather information to the user in string format


Example 1:
START : Hey can you solve 2+3 * 5/10
PLAN:{"step":"PLAN","content":"Seems lik user is interested in math problem"  }
PLAN:{"step":"PLAN","content":"Looks like problem can be solved using BODMAS method"  }
PLAN:{"step":"PLAN","content":"Yes the  problem can be solved using BODMAS method"  }

PLAN:{"step":"PLAN","content":"First we mutlipy 3 *5 which give 15"  }

PLAN:{"step":"PLAN","content":"Then we divide 15 which give 10 which give 1.5"  }

PLAN:{"step":"PLAN","content":"Then we add 1.5 with 2 give 3.5"  }

OUTPUT:{"step":"OUTPUT","content":"3.5"  }


Example 2:
START : What is the weather of Delhi
PLAN:{"step":"PLAN","content":"Seems lik user is interested in getting the weather of Delhi in India"  }

PLAN:{"step":"PLAN","content":"Let see if we have any available tool from the list of available tools"  }

PLAN:{"step":"PLAN","content":"
Great we have get_weather tool available for this query."  }

PLAN:{"step":"PLAN","content":"I need to call get_weather tool for Delhi as input for city"  }

PLAN:{"step":"TOOL","tool":"get_weather", "input":"delhi"  }

PLAN:{"step":"OBSERVE","tool":"get_weather","output":"The temprature of delhi is fog with 12 C"  }
PLAN:{"step":"PLAN","content":"Great , I got the temprature info about delhi"  }

OUTPUT:{"step":"OUTPUT","content":"The current temprature in delhi is 12 C with foggy weather."  }

"""


def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return (f"Weather in {city.lower()} is {response.text}")
    return "Something went wrong"


available_tools = {
    "get_weather": get_weather
}

messageHistory = [
    {"role": "system", "content": SYSTEM_PROMPT},
]
user_query = input("👉")
messageHistory.append({"role": "user", "content": user_query})
while True:

    response = client.chat.completions.parse(
        model="gpt-5-mini",
        response_format={"type": "json_object"},

        messages=messageHistory)

    raw_data = response.choices[0].message.content
    pasrsed_data = json.loads(raw_data)

    state = pasrsed_data["step"]
    if state == "START":
        print(f"🔥 {pasrsed_data["content"]}")
        messageHistory.append({
            "role": "assistant",
            "content": raw_data   # MUST be string
        })
        continue
    if state == "PLAN":
        print(f"🧠 {pasrsed_data["content"]}")
        messageHistory.append({
            "role": "assistant",
            "content": raw_data   # MUST be string
        })
        continue
    if state == "TOOL":
        tool_to_call = pasrsed_data["tool"]
        tool_input = pasrsed_data["input"]
        print(f"⚙️ {tool_to_call},{tool_input}")
        tool_response = available_tools[tool_to_call](tool_input)
        print(f"⚙️ {tool_to_call},{tool_input}={tool_response}")
        messageHistory.append({
            "role": "developer",
            "content": json.dumps(
                {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input,
                    "output": tool_response}
            )  # MUST be string
        })
        continue
    if state == "OUTPUT":
        print(f"💪 {pasrsed_data["content"]}")
        break
