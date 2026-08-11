from langgraph.graph import StateGraph, START, END

from state import AgentState
from planner import planner
from agents import research_agent, database_agent, tool_agent

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner)
workflow.add_node("research", research_agent)
workflow.add_node("database", database_agent)
workflow.add_node("tool", tool_agent)


workflow.add_edge(START, "planner")

def route_agent(state):
    return state["agent"]


workflow.add_conditional_edges(
    "planner",
    route_agent,
    {
        "research": "research",
        "database": "database",
        "tool": "tool"
    }
)

workflow.add_edge("research", END)
workflow.add_edge("database", END)
workflow.add_edge("tool", END)

graph = workflow.compile()