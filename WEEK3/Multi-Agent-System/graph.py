from langgraph.graph import StateGraph, START, END

from state import AgentState
from agents import supervisor, researcher, coder, reviewer

workflow = StateGraph(AgentState)

workflow.add_node("supervisor", supervisor)
workflow.add_node("researcher", researcher)
workflow.add_node("coder", coder)
workflow.add_node("reviewer", reviewer)

workflow.add_edge(START, "supervisor")

workflow.add_edge("supervisor", "researcher")
workflow.add_edge("researcher", "coder")
workflow.add_edge("coder", "reviewer")
workflow.add_edge("reviewer", END)

graph = workflow.compile()