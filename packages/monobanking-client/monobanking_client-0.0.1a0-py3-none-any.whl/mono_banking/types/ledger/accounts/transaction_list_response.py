# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TransactionListResponse", "Pagination", "Transaction", "TransactionAmount"]


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

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class Transaction(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    amount: Optional[TransactionAmount] = None
    """Money schema"""

    description: Optional[str] = None
    """useful infomation about the transaction"""

    id_in_origin: Optional[str] = None
    """String field"""

    operation_type: Optional[Literal["debit", "credit", "hold", "release"]] = None
    """The four common transaction operations are credit, debit, hold, and release:

    - credit: Increases the balance of the account. It is typically used to
      represent income.
    - debit: Decreases the balance of the account. It is typically used to represent
      expenses.
    - hold: Setting aside of funds for a specific purpose, such as a pending
      transaction.
    - release: Represent the release of previously held funds for a pending
      transaction.
    """

    origin: Optional[str] = None
    """The operation from which the transaction originated"""

    origin_transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was created"""

    reverted_by_id: Optional[str] = None
    """The ID of the transaction that reverts this ledger transaction"""

    reverts_id: Optional[str] = None
    """The ID of the transaction that this ledger transaction reverts"""

    transaction_at: Optional[datetime] = None
    """Date and Time at which the transaction was actually performed"""


class TransactionListResponse(BaseModel):
    pagination: Optional[Pagination] = None
    """Pagination schema"""

    transactions: Optional[List[Transaction]] = None
    """Contains a set of transactions."""
