from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Custom MCP Server")


@mcp.tool()
def add(a:int, b:int)->int:
    """Add two numbers."""
    return a+b


@mcp.tool()
def multiply(a:int, b:int)->int:
    """Multiply two numbers."""
    return a*b


@mcp.tool()
def greet(name:str)->str:
    """Greet a user."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print("Custom MCP Server is running...")
    mcp.run()