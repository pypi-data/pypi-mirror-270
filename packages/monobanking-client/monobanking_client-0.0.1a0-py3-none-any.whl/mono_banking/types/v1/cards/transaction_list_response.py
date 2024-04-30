# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TransactionListResponse", "Pagination", "Transaction", "TransactionAmount", "TransactionGmfAmount"]


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class TransactionAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class TransactionGmfAmount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class Transaction(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[TransactionAmount] = None
    """Transaction amount"""

    declination_reason: Optional[str] = None
    """String field"""

    description: Optional[str] = None
    """String field"""

    gmf_amount: Optional[TransactionGmfAmount] = None
    """GMF amount"""

    operation_type: Optional[Literal["debit", "credit"]] = None
    """Transaction operation type"""

    state: Optional[Literal["approved", "reversed", "declined"]] = None
    """State of the card transaction"""

    transaction_at: Optional[datetime] = None
    """Date and time when the card transaction was made"""


class TransactionListResponse(BaseModel):
    card_id: Optional[str] = None
    """Card ID"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""

    transactions: Optional[List[Transaction]] = None
    """It contains a list with card transactions"""
