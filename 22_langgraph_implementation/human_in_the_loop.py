from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool
from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from langchain.messages import HumanMessage, AnyMessage
from langgraph.types import Command, interrupt
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model="gpt-5-nano"

)


class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]


# tool.invoke("Difference btween langchain and langgraph")


@tool
def human_assistance(query: str):
    """Request assistance from human"""
    human_resposne = interrupt({"query": query})
    return human_resposne["data"]


tool = TavilySearch(max_results=2)
tools = [tool, human_assistance]
llm_with_tools = llm.bind_tools(tools)

graph_builder = StateGraph(AgentState)


def chatbot(state: AgentState):
    return {
        "messages": llm_with_tools.invoke(state["messages"])
    }


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")

graph = graph_builder.compile()

config = {
    "configurable": {
        "thread_id": "2"
    }
}

user_input = "I need some expert guidance and assistance for building an ai agent. could you request assistance for me"

events = graph.stream({
    "messages": [HumanMessage(content=user_input)]},
    config=config,
    stream_mode="values"
)
for event in events:
    if "messages" in event:
        print(event["messages"][-1])

print("\n\n\n\n")
human_response = (
    "We , the experts are here to help! we'd recommend you check out Langgraph tp build your agent."
)

human_command = Command(resume={"data": human_response})

events = graph.stream(
    human_command,
    config=config,
    stream_mode="values"
)
for event in events:
    if "messages" in event:
        print(event["messages"][-1])
