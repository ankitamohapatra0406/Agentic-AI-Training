from state import AgentState


def supervisor(state: AgentState):
    print("\n[Supervisor Agent]")
    return state


def researcher(state: AgentState):
    print("\n[Research Agent]")

    return {
        "research": f"Research completed for: {state['question']}"
    }


def coder(state: AgentState):
    print("\n[Coding Agent]")

    return {
        "code": f"Sample code generated for: {state['question']}"
    }


def reviewer(state: AgentState):
    print("\n[Reviewer Agent]")

    report = f"""
FINAL REPORT

Research:
{state['research']}

Code:
{state['code']}
"""

    return {
        "review": report
    }