# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ListTargetRetrieveResponse", "Card", "Pagination"]


class Card(BaseModel):
    id: Optional[str] = None
    """Card ID"""

    account_id: Optional[str] = None
    """Account ID"""

    last_four: Optional[str] = None
    """Last four digits of the card"""

    nickname: Optional[str] = None
    """Card nickname"""

    state: Optional[Literal["active", "frozen", "canceled", "created"]] = None
    """State of the card"""


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class ListTargetRetrieveResponse(BaseModel):
    cards: Optional[List[Card]] = None
    """It contains a list with spending controls cards"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""
