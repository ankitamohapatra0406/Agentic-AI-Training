def calculate(expression):
    try:
        allowed="0123456789+-*/(). "
        
        if not all(char in allowed for char in expression):
            return "Invalid expression"

        result = eval(expression)
        return f"Result: {result}"

    except Exception:
        return "Could not calculate the expression"

def search_information(topic):
    return f"Research result for: {topic}"


def database_lookup(query):
    data = {
        "student": "Student records are stored in the database.",
        "course": "Available courses include Computer Science and Data Science."
    }

    query=query.lower()

    for key, value in data.items():
        if key in query:
            return value

    return "No matching database record found."