from state import AgentState


def planner(state: AgentState):
    print("\n[Planner Node]")

    question = state["question"]

    plan = f"Research the topic: {question}"

    return {
        "plan": plan
    }


def researcher(state: AgentState):
    print("\n[Research Node]")

    plan = state["plan"]

    research = f"Detailed research completed for '{plan}'"

    return {
        "research": research
    }


def tool_agent(state: AgentState):
    print("\n[Tool Agent Node]")

    question = state["question"]

    answer = f"Quick answer for: {question}"

    return {
        "answer": answer
    }


def final_node(state: AgentState):
    print("\n[Final Node]")

    if state.get("research"):
        answer = state["research"]
    else:
        answer = state["answer"]

    return {
        "answer": answer
    }
def route_question(state: AgentState):

    question = state["question"]

    if len(question.split()) > 5:
        return "research"

    return "tool"