"""Open Library MCP Server - Simple beginner-friendly implementation."""

import httpx
#from fastmcp import FastMCP
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("open-library")

# API Configuration
BASE_URL = "https://openlibrary.org"
SEARCH_ENDPOINT = f"{BASE_URL}/search.json"


async def search_open_library(title=None, author=None, year=None, limit=10):
    """Search the Open Library API and return results."""
    # Build the search query
    query_parts = []
    if title:
        query_parts.append(f'title:"{title}"')
    if author:
        query_parts.append(f'author:"{author}"')
    if year:
        query_parts.append(f"first_publish_year:{year}")

    query = " AND ".join(query_parts) if query_parts else "*"

    # Make the API request
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            SEARCH_ENDPOINT,
            params={"q": query, "limit": min(limit, 100)}
        )
        response.raise_for_status()
        data = response.json()

    # Return the results directly from the API
    return {
        "total_found": data.get("numFound", 0),
        "books": data.get("docs", [])
    }


# MCP Tools - These are the functions Claude can use
@mcp.tool()
async def list_books_by_month(year: int, month: int, limit: int = 10):
    """List books published in a specific month and year.

    Note: Open Library API only supports year filtering, not specific months.

    Args:
        year: Publication year (e.g., 2020)
        month: Publication month (1-12)
        limit: Maximum results to return (default: 10, max: 100)
    """
    # Validate inputs
    if not 1 <= month <= 12:
        raise ValueError(f"Month must be between 1 and 12, got {month}")

    if year < 1000 or year > 9999:
        raise ValueError(f"Year must be a valid 4-digit year, got {year}")

    # Search for books from that year
    result = await search_open_library(year=year, limit=limit)

    return {
        "message": (
            f"Found {result['total_found']} books from {year}. "
            f"Showing {len(result['books'])} results. "
            "(Note: API only supports year-level filtering)"
        ),
        "total_found": result["total_found"],
        "books": result["books"],
    }


@mcp.tool()
async def search_books(title: str, limit: int = 10):
    """Search for books by title.

    Args:
        title: Book title to search for
        limit: Maximum results to return (default: 10, max: 100)
    """
    if not title.strip():
        raise ValueError("Title cannot be empty")

    result = await search_open_library(title=title, limit=limit)

    return {
        "message": (
            f"Found {result['total_found']} books matching '{title}'. "
            f"Showing {len(result['books'])} results."
        ),
        "total_found": result["total_found"],
        "books": result["books"],
    }


@mcp.tool()
async def search_books_by_author(author: str, limit: int = 10):
    """Search for books by author name.

    Args:
        author: Author name to search for
        limit: Maximum results to return (default: 10, max: 100)
    """
    if not author.strip():
        raise ValueError("Author name cannot be empty")

    result = await search_open_library(author=author, limit=limit)

    return {
        "message": (
            f"Found {result['total_found']} books by '{author}'. "
            f"Showing {len(result['books'])} results."
        ),
        "total_found": result["total_found"],
        "books": result["books"],
    }


@mcp.tool()
async def get_book_by_work_key(work_key: str):
    """Get detailed information about a book using its Open Library work key.

    Args:
        work_key: Open Library work key (e.g., 'OL45804W' or '/works/OL45804W')
    """
    if not work_key.strip():
        raise ValueError("Work key cannot be empty")

    # Ensure key starts with /works/
    if not work_key.startswith("/works/"):
        work_key = f"/works/{work_key}"

    url = f"{BASE_URL}{work_key}.json"

    # Fetch the book details
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        details = response.json()

        return {
            "message": f"Retrieved details for {work_key}",
            "book": details,
        }


if __name__ == "__main__":
    mcp.run()
