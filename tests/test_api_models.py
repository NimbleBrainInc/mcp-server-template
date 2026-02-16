"""Tests for Example API models."""

from mcp_example.api_models import Item, ItemListResponse, Pagination


def test_item_model() -> None:
    """Test Item model parsing from API response."""
    data = {
        "id": "item_123",
        "name": "Test Item",
        "description": "A test item",
        "createdAt": "2026-01-01T00:00:00Z",
        "updatedAt": "2026-01-02T00:00:00Z",
        "metadata": {"key": "value"},
    }
    item = Item(**data)
    assert item.id == "item_123"
    assert item.name == "Test Item"
    assert item.created_at == "2026-01-01T00:00:00Z"
    assert item.metadata == {"key": "value"}


def test_item_model_minimal() -> None:
    """Test Item model with only required fields."""
    item = Item(id="item_456")
    assert item.id == "item_456"
    assert item.name is None
    assert item.metadata == {}


def test_pagination_model() -> None:
    """Test Pagination model."""
    data = {"nextCursor": "abc123", "hasMore": True}
    pagination = Pagination(**data)
    assert pagination.next_cursor == "abc123"
    assert pagination.has_more is True


def test_pagination_defaults() -> None:
    """Test Pagination model defaults."""
    pagination = Pagination()
    assert pagination.next_cursor is None
    assert pagination.has_more is False


def test_item_list_response() -> None:
    """Test ItemListResponse model."""
    data = {
        "items": [
            {"id": "1", "name": "First"},
            {"id": "2", "name": "Second"},
        ],
        "pagination": {"nextCursor": "next", "hasMore": True},
    }
    response = ItemListResponse(**data)
    assert len(response.items) == 2
    assert response.items[0].id == "1"
    assert response.pagination.has_more is True


def test_item_list_response_empty() -> None:
    """Test ItemListResponse with empty results."""
    response = ItemListResponse()
    assert response.items == []
    assert response.pagination.has_more is False
