"""Tests for Example MCP Server tools."""

import pytest
from unittest.mock import AsyncMock, patch

from mcp_example.api_client import ExampleAPIError


@pytest.fixture
def mock_client():
    """Create a mock API client."""
    client = AsyncMock()
    client.list_items = AsyncMock(return_value=[
        {"id": "1", "name": "Item 1"},
        {"id": "2", "name": "Item 2"},
    ])
    client.get_item = AsyncMock(return_value={
        "id": "1",
        "name": "Item 1",
        "description": "Test item",
    })
    return client


@pytest.mark.asyncio
async def test_list_items(mock_client):
    """Test list_items tool."""
    with patch("mcp_example.server.get_client", return_value=mock_client):
        from mcp_example.server import list_items
        result = await list_items(limit=10)
        assert len(result) == 2
        mock_client.list_items.assert_called_once_with(limit=10)


@pytest.mark.asyncio
async def test_get_item(mock_client):
    """Test get_item tool."""
    with patch("mcp_example.server.get_client", return_value=mock_client):
        from mcp_example.server import get_item
        result = await get_item(item_id="1")
        assert result["id"] == "1"
        mock_client.get_item.assert_called_once_with("1")


@pytest.mark.asyncio
async def test_list_items_api_error(mock_client):
    """Test list_items handles API errors."""
    mock_client.list_items = AsyncMock(
        side_effect=ExampleAPIError(401, "Unauthorized")
    )
    with patch("mcp_example.server.get_client", return_value=mock_client):
        from mcp_example.server import list_items
        with pytest.raises(ExampleAPIError):
            await list_items()
