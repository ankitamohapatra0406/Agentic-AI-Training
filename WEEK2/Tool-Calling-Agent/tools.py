from langchain_core.tools import tool
from datetime import datetime

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

@tool
def today(dummy: str = "") -> str:
    """Returns today's date."""
    return datetime.now().strftime("%d-%m-%Y")