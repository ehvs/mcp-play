# Quick Start Guide

## 1. Install Dependencies

```bash
pip install fastmcp httpx pydantic
```

## 2. Run the Server

```bash
cd python-open-library-mcp
python src/server.py
```

## 3. Test It

The server will start and wait for MCP connections.

## 4. Use with Claude Desktop

Edit your Claude Desktop config file and add:

```json
{
  "mcpServers": {
    "open-library": {
      "command": "python",
      "args": ["/absolute/path/to/python-open-library-mcp/src/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/` with the actual path to your project.

## 5. Try It in Claude

After restarting Claude Desktop, you can ask:

- "List books from January 2020"
- "Search for books titled 'The Hobbit'"
- "Find books by Neil Gaiman"
- "Get details for work key OL27482W"

## That's it!

Everything is in a single file: `src/server.py` (240 lines)
