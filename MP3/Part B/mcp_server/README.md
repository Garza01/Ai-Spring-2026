# MiniClaw MCP Server

Chosen host for the documented review: **Codex local MCP-style test harness**.
The same server is ready for Claude Desktop, Cursor, or VS Code Copilot once
`fastmcp` / `mcp` is installed from `requirements.txt`.

## Run

```bash
pip install -r "MP3/Part B/mcp_server/requirements.txt"
python "MP3/Part B/mcp_server/server.py"
```

## Copyable Host Config

```json
{
  "mcpServers": {
    "miniclaw-knowledge": {
      "command": "python3",
      "args": [
        "/Users/albertogarza/Ai-Spring-2026/MP3/Part B/mcp_server/server.py"
      ]
    }
  }
}
```

## Evidence

- `logs/server.log` contains the tool invocations used in the CAD review.
- `conversation_export.md` contains one end-to-end exchange.
- `screenshots/` contains host-style captures showing the tool call indicator.
