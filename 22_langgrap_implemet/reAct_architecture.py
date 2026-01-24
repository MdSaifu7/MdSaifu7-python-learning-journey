from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from langchain.messages import HumanMessage, AnyMessage
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model="gpt-5-nano"

)


class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]


tool = TavilySearch(max_results=2)
# tool.invoke("Difference btween langchain and langgraph")


def multiply(a: int, b: int) -> int:
    """
    Multipy a and b

    args:
    first int= a,
    first int =b

    return :
    int : output
    """
    return a*b


tools = [tool, multiply]
llm_with_tools = llm.bind_tools(tools)

graph_builder = StateGraph(AgentState)


def tool_calling_llm(state: AgentState):
    return {
        "messages": llm_with_tools.invoke(state["messages"])
    }


graph_builder.add_node("tool_calling_llm", tool_calling_llm)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "tool_calling_llm")
graph_builder.add_conditional_edges("tool_calling_llm", tools_condition)
graph_builder.add_edge("tools", "tool_calling_llm")

graph = graph_builder.compile()

res = graph.invoke({
    "messages": [HumanMessage(content="Tell me about new instafram feature and what is 2*10")]
})

print(res["messages"][-1].content)
