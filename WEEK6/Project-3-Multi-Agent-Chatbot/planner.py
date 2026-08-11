def planner(state):
    question=state["question"]

    question_lower=question.lower()

    if any(word in question_lower for word in [
        "search",
        "research",
        "latest",
        "news",
        "who",
        "when",
        "where"
    ]):
        agent="research"

    elif any(word in question_lower for word in [
        "database",
        "record",
        "student",
        "user",
        "data"
    ]):
        agent="database"

    else:
        agent="tool"

    return {
        "plan": f"Route the question to the {agent} agent.",
        "agent": agent
    }