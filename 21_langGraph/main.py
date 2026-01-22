from dotenv import load_dotenv
import os
from langgraph.graph import StateGraph
from langchain.messages import HumanMessage, SystemMessage
from typing import TypedDict, List
from langchain_openai import ChatOpenAI
load_dotenv()
llm = ChatOpenAI(
    model="gpt-5",
    api_key=os.getenv("OPENAI_API_KEY")
)


class AgentState(TypedDict):
    question: str
    thoughts: List[str]
    answer: str


# Nodes

def think_node(state: AgentState):

    messages = [
        SystemMessage(
            content="I m a helpful ai assintant, which resolves user query"),
        HumanMessage(content=state["question"])
    ]
    response = llm.invoke(messages)
    state["thoughts"].append(response.content)
    return state


def decide_node(state: AgentState):
    state["thoughts"].append("User has asked conceptual/bussiness question.")

    return state


def ans_node(state: AgentState):

    messages = [
        SystemMessage(
            content="I m a helpful ai assintant, which resolves user query"),
        HumanMessage(content=f"""

    Question: {state["question"]}
    thoughts so far :{state['thoughts']} .
    Now give a clear final answer
    
    """)

    ]
    response = llm.invoke(messages)
    state["answer"] = response.content
    return state


graph = StateGraph(AgentState)

graph.add_node("think", think_node)
graph.add_node("decide", decide_node)
graph.add_node("answer", ans_node)

graph.set_entry_point("think")
graph.add_edge("think", "decide")
graph.add_edge("decide", "answer")
graph.set_finish_point("answer")

app = graph.compile()
result = app.invoke({
    "question": "Why blackberry shutdown",
    "thoughts": [],
    "answer": ""
})

print("Thoughts:", result["thoughts"])
print("Answer:", result["answer"])
