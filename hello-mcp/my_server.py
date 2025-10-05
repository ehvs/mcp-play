from fastmcp import FastMCP

mcp = FastMCP("my mcp server")

@mcp.tool
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

#The __main__ block is recommended for consistency and compatibility, 
# ensuring your server works with all MCP clients that execute your server file as a script.
# Users who will exclusively run their server with the FastMCP CLI can omit it, 
# as the CLI imports the server object directly.
if __name__ == "__main__":
    mcp.run()