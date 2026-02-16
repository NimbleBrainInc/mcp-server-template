"""Pydantic models for Example API responses.

Replace these with models matching your actual API response schemas.
"""

from typing import Any

from pydantic import BaseModel, Field


# ============================================================================
# Common Models
# ============================================================================


class Pagination(BaseModel):
    """Pagination information."""

    model_config = {"populate_by_name": True}

    next_cursor: str | None = Field(default=None, alias="nextCursor", description="Next page cursor")
    has_more: bool = Field(default=False, alias="hasMore", description="Whether more pages exist")


# ============================================================================
# Resource Models - Replace with your API's models
# ============================================================================


class Item(BaseModel):
    """An item from the Example API."""

    id: str = Field(..., description="Item ID")
    name: str | None = Field(None, description="Item name")
    description: str | None = Field(None, description="Item description")
    created_at: str | None = Field(None, alias="createdAt", description="Created timestamp")
    updated_at: str | None = Field(None, alias="updatedAt", description="Updated timestamp")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata")


class ItemListResponse(BaseModel):
    """Response for listing items."""

    items: list[Item] = Field(default_factory=list)
    pagination: Pagination = Field(default_factory=lambda: Pagination())


class ItemResponse(BaseModel):
    """Response for a single item."""

    data: Item


# ============================================================================
# Error Models
# ============================================================================


class ErrorDetail(BaseModel):
    """Error detail."""

    code: str | None = Field(None, description="Error code")
    message: str | None = Field(None, description="Error message")
    request_id: str | None = Field(None, alias="requestId", description="Request ID")
