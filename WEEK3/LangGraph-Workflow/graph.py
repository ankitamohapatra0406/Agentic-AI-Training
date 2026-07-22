from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes import (
    planner,
    researcher,
    tool_agent,
    final_node,
    route_question,
)

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner)
workflow.add_node("researcher", researcher)
workflow.add_node("tool", tool_agent)
workflow.add_node("final", final_node)

workflow.add_edge(START, "planner")

workflow.add_conditional_edges(
    "planner",
    route_question,
    {
        "research": "researcher",
        "tool": "tool",
    },
)

workflow.add_edge("researcher", "final")
workflow.add_edge("tool", "final")
workflow.add_edge("final", END)

graph = workflow.compile()