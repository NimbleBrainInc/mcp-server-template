# Example MCP Server

An MCP (Model Context Protocol) server that provides access to the Example API, allowing AI assistants to interact with Example data.

## Features

- List and retrieve items from the Example API
- Async HTTP client with error handling
- Typed responses with Pydantic models

## Installation

### Using mpak (Recommended)

```bash
# Configure your API key
mpak config set @nimblebraininc/example api_key=your_api_key_here

# Run the server
mpak run @nimblebraininc/example
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/NimbleBrainInc/mcp-example.git
cd mcp-example

# Install dependencies with uv
uv sync

# Set your API key
export EXAMPLE_API_KEY=your_api_key_here

# Run the server
uv run python -m mcp_example.server
```

## Configuration

### Getting Your API Key

1. Go to https://example.com/settings/api
2. Create a new API key
3. Copy the key

### Claude Desktop Configuration

Add to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "example": {
      "command": "mpak",
      "args": ["run", "@nimblebraininc/example"]
    }
  }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `list_items` | List items from the API with optional limit |
| `get_item` | Get a single item by its ID |

## Development

```bash
# Install dev dependencies
uv sync --dev

# Run tests
uv run pytest tests/ -v

# Format code
uv run ruff format src/ tests/

# Lint
uv run ruff check src/ tests/

# Type check
uv run ty check src/

# Run all checks
make check
```

## License

MIT
