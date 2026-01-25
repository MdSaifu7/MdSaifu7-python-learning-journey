from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from langchain.messages import HumanMessage, AnyMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model="gpt-5-nano"

)

memory = MemorySaver()


class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]





graph_builder = StateGraph(AgentState)


def superbot(state: AgentState):
    return {
        "messages": llm.invoke(state["messages"])
    }


graph_builder.add_node("superbot", superbot)


graph_builder.add_edge(START, "superbot")

graph_builder.add_edge("superbot", END)

graph = graph_builder.compile(checkpointer=memory)


config = {
    "configurable": {
        "thread_id": "3"
    }
}

for chunk in graph.stream({"messages": [
    SystemMessage(content="You give output less than or equall to 100 words"),
    HumanMessage(
        content="My name is Saif . I will be the best coder in the history.")

]}, config, stream_mode="updates"):
    print(chunk)
print("\n\n\n\n")

for chunk in graph.stream({"messages": "I m into fitness too."}, config, stream_mode="values"):
    print(chunk)
