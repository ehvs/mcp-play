from mcp.server.fastmcp import FastMCP

# create an mcp server instance
mcp = FastMCP("My weather MCP Service")

# Tool implementation - ACTIONS!
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # In a real implementation, you would call a weather API here.
    # For demonstration purposes, we'll return a mock response.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

# Resource implementation - DATA!
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Resource to get weather information for a given location."""
    return f"Weather data for {location}: Sunny, 25°C."

#Prompt implementation - PROMPTS!
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""

# Run the server
if __name__ == "__main__":
    mcp.run()