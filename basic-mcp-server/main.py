import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='mcp_server.log',
    filemode='a' # append mode
    )

from mcp.server.fastmcp import FastMCP,Context
import time
from datetime import datetime

mcp = FastMCP(name="CalcStuff")

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"Error [{code}]: {message}")



logger = logging.getLogger(__name__)

# functions/methods
@mcp.tool()
# this exposes the function as a tool in the MCP server
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The sum of the two integers
    """
    logger.info(f"Adding {a} and {b}")
    result = a + b
    logger.info(f"Result: {result}")
    return result

@mcp.tool()
def divide(a: int, b: int) -> float:
    """
    Divide two integers.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        float: The division of the two integers
    """
    if b == 0:
        raise MCPError(code=400, message="Division by zero is not allowed.")
    return a / b

@mcp.tool()
def long_process(steps: int):
    """
    Simulate a long running process.
    """
    start = datetime.now()
    print(f"Starting at: {start}")
    for i in range(steps):
        print(f"Processing step {i+1}/{steps}")
        time.sleep(0.1)  # simulate work
    end = datetime.now()
    duration = end - start
    return f"Process completed. Started at: {start}, Ended at: {end}, Duration: {duration}"



if __name__ == "__main__":
    mcp.run(transport='stdio') # run the MCP server using stdio transport
    logging.shutdown()
