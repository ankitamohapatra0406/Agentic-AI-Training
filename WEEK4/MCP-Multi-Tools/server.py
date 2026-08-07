from mcp.server.fastmcp import FastMCP

from tools import (
    add,
    multiply,
    read_notes,
    save_user,
    get_users,
)

mcp=FastMCP("MCP Multi Tool Server")

mcp.tool()(add)
mcp.tool()(multiply)
mcp.tool()(read_notes)
mcp.tool()(save_user)
mcp.tool()(get_users)

if __name__ == "__main__":
    print("MCP Multi Tool Server Running...")
    mcp.run()