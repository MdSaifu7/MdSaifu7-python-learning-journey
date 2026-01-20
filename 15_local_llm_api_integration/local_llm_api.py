from fastapi import FastAPI, Body
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"


class PromptRequest(BaseModel):
    prompt: str


class AIResponse(BaseModel):
    response: str


@app.post("/res", response_model=AIResponse)
def res(message: str = Body(..., description="The Message")):
    payload = {
        "model": "phi3",
        "prompt": message,
        "stream": False
    }
    result = requests.post(OLLAMA_URL, json=payload)
    result = result.json()
    print(result["response"])
    return {
        "response": result["response"]
    }


@app.post("/chat", response_model=AIResponse)
def chat_with_ai(data: PromptRequest):
    payload = {
        "model": "llama3",
        "prompt": data.prompt,
        "stream": False
    }

    res = requests.post(OLLAMA_URL, json=payload)

    result = res.json()

    return {
        "response": result["response"]
    }
