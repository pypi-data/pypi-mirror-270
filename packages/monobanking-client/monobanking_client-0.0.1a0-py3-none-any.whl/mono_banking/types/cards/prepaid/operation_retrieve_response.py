# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OperationRetrieveResponse", "BalanceOperation", "BalanceOperationAmount", "Pagination"]


class BalanceOperationAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class BalanceOperation(BaseModel):
    amount: BalanceOperationAmount
    """deposit balance amount"""

    operation: Literal["topup", "withdrawal"]
    """there are two operation types:

    - topup: Increments the card balance.
    - withdrawal: Reduces the card balance.
    """

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    card_id: Optional[str] = None
    """Indicates the format for resource's ID"""

    description: Optional[str] = None
    """String field"""

    entity_id: Optional[str] = None
    """String field"""

    performed_at: Optional[datetime] = None
    """Date and time when the card balance operation was performed"""


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class OperationRetrieveResponse(BaseModel):
    balance_operations: Optional[List[BalanceOperation]] = None
    """It contains a list with card balance operations"""

    card_id: Optional[str] = None
    """Card ID"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""
