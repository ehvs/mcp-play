from os import name
from fastmcp import FastMCP
import sqlite3
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "community.db")

mcp = FastMCP("sqlite-server")

@mcp.tool()
def get_tables():
    """Retrieve the tables from the database."""
    # connect to the database
    conn = sqlite3.connect(DB_PATH)
    # create a cursor object
    cursor = conn.cursor()
    # execute the query
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    results = cursor.fetchall()
    conn.close()
    # format as a list of dictionaries
    tables = [{"name": name} for name in results]
    return tables

@mcp.tool()
def get_top_chatters():
    """Retrieve the top 10 chatters from the database."""
    # connect to the database
    print(f"DEBUG: Connecting to database at: {DB_PATH}", flush=True)
    print(f"DEBUG: Database exists: {os.path.exists(DB_PATH)}", flush=True)
    conn = sqlite3.connect(DB_PATH)
    # create a cursor object
    cursor = conn.cursor()
    # execute the query
    cursor.execute("SELECT name, messages FROM chatters ORDER BY messages DESC")
    results = cursor.fetchall()
    conn.close()
    # format as a list of dictionaries
    chatters = [{"name": name, "messages": messages} for name, messages in results]
    return chatters

# Run the MCP server locally
if __name__ == "__main__":
    mcp.run()
