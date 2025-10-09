# mcp-play
Playground for MCP projects

## Nice repos

- https://opentools.com/registry?category=api
- https://gofastmcp.com/getting-started/welcome
- https://github.com/adhikasp/mcp-weather
- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/modelcontextprotocol/servers

# Bins
We'll use a lot of libraries from python, is recommended to use a virtual package manager. Check the **Diagram** session on the bottom for more details.

## UV (Recommended)
- uv `curl -LsSf https://astral.sh/uv/install.sh | sh` | [docs - astral.sh](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
    - uv pip install fastmcp
    - uv pip install mcp[cli]
    - uv pip install cmcp

## Conda
- `conda create -n basicserver312 python=3.12`
- `conda activate basicserver312`
- `conda install mcp fastmcp`
- `pip install cmcp`

# About It
## Types of MCP
It can be stdio/SSE/HTTPs

### Type STDIO
- Less overhead, perfect for cli and dev tools.

### Type SSE
- Small overhead, perfect for persistent connections like chatbots.

# Testing
## mcp dev
It will expose MCP Inspector on localhost port 6277
- How to use
```
mcp dev main.py
```

## cmcp - Install with pip
- How to use
```
$ cmcp 'python3 main.py' tools/call name=add arguments:='{"a": 2, "b": 3}'
{
  "content": [
    {
      "type": "text",
      "text": "5"
    }
  ],
  "structuredContent": {
    "result": 5
  }
}
```

# Diagrams for pkg mgmt
## Conda
```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONDA PACKAGE MANAGEMENT                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌────────────────────────────────────────────────────────┐        │
│  │              Conda Environment                         │        │
│  │                                                        │        │
│  │  ┌──────────────────┐      ┌──────────────────┐       │        │
│  │  │ Conda Packages   │      │   Pip Packages   │       │        │
│  │  │                  │      │                  │       │        │
│  │  │ • Python itself  │      │ • PyPI packages  │       │        │
│  │  │ • System libs    │      │ • Pure Python    │       │        │
│  │  │ • Binary deps    │◄─────┤ • Wheels         │       │        │
│  │  │ • NumPy, etc.    │ deps │                  │       │        │
│  │  └──────────────────┘      └──────────────────┘       │        │
│  │                                                        │        │
│  │  Isolated from system Python & system packages        │        │
│  └────────────────────────────────────────────────────────┘        │
│                          ▲                                          │
│                          │                                          │
│                  ┌───────┴────────┐                                 │
│                  │  Conda solves  │                                 │
│                  │  dependencies  │                                 │
│                  │  across both   │                                 │
│                  └────────────────┘                                 │
└─────────────────────────────────────────────────────────────────────┘
```
## UV
```
┌─────────────────────────────────────────────────────────────────────┐
│                      UV PACKAGE MANAGEMENT                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌────────────────────────────────────────────────────────┐        │
│  │              UV Virtual Environment                    │        │
│  │                                                        │        │
│  │  ┌──────────────────┐      ┌──────────────────┐       │        │
│  │  │   Python Venv    │      │   Pip Packages   │       │        │
│  │  │                  │      │                  │       │        │
│  │  │ Uses system or   │      │ • PyPI packages  │       │        │
│  │  │ downloaded       │      │ • Wheels/sdist   │       │        │
│  │  │ Python binary    │◄─────┤ • Fast install   │       │        │
│  │  │                  │ uses │ • Rust-powered   │       │        │
│  │  └──────────────────┘      └──────────────────┘       │        │
│  │                                                        │        │
│  │  Isolated Python packages only                        │        │
│  └────────────────────────────────────────────────────────┘        │
│                          ▲                                          │
│             ┌────────────┴────────────┐                             │
│             │  System packages for    │                             │
│             │  non-Python deps        │                             │
│             │  (apt, dnf, brew, etc.) │                             │
│             └─────────────────────────┘                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```