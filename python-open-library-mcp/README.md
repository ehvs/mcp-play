# Open Library MCP Server

A simple MCP server that provides tools to search and retrieve book information from the Open Library API.

## Installation

```bash
# Install dependencies
pip install fastmcp httpx

# Or install the package
pip install -e .
```

## Running the Server

```bash
python src/server.py
```

## Configuration for Claude Desktop

Add this to your Claude Desktop config:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "open-library": {
      "command": "python",
      "args": ["/full/path/to/python-open-library-mcp/src/server.py"]
    }
  }
}
```

## Available Tools

### 1. `list_books_by_month`
Search for books published in a specific month and year.

**Parameters:**
- `year` (int): Publication year (e.g., 2020)
- `month` (int): Publication month (1-12)
- `limit` (int): Maximum results (default: 10, max: 100)

**Example:**
```
List books from March 2020
```

### 2. `search_books`
Search for books by title.

**Parameters:**
- `title` (str): Book title to search for
- `limit` (int): Maximum results (default: 10, max: 100)

**Example:**
```
Search for books with title "The Hobbit"
```

### 3. `search_books_by_author`
Search for books by author name.

**Parameters:**
- `author` (str): Author name to search for
- `limit` (int): Maximum results (default: 10, max: 100)

**Example:**
```
Find books by Neil Gaiman
```

### 4. `get_book_by_work_key`
Get detailed information about a specific book.

**Parameters:**
- `work_key` (str): Open Library work key (e.g., "OL45804W")

**Example:**
```
Get details for book with work key OL27482W
```

## Project Structure

```
python-open-library-mcp/
├── src/
│   └── server.py       # Main MCP server (single file)
├── pyproject.toml      # Dependencies
└── README.md           # This file
```

## How It Works

The server uses:
- **FastMCP** - Framework for building MCP servers
- **httpx** - Async HTTP client for API requests
- **Pydantic** - Data validation and models

All code is in a single file (`src/server.py`) for simplicity.
