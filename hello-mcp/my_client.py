import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    # We must enter a client context (async with client:) before using the client
    async with client:
        response = await client.call_tool("greet", {"name": name})
        print(response)
#FastMCP clients are asynchronous, so we need to use asyncio.run to run the client
asyncio.run(call_tool("Alice"))