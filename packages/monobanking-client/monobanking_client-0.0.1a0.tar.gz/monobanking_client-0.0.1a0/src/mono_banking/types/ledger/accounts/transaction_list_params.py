# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TransactionListParams", "OriginTransactionAt", "Sort", "TransactionAt"]


class TransactionListParams(TypedDict, total=False):
    operation_type: Union[
        List[Literal["debit", "credit", "hold", "release"]], Literal["debit", "credit", "hold", "release"]
    ]
    """Filters by the four operations available (credit, debit, hold and release)"""

    origin: Union[List[str], str]
    """Filters by the origins like `card_transaction`, `card_authorization`, etc."""

    origin_transaction_at: OriginTransactionAt
    """Filters the transactions by date time ranges when the transaction was created"""

    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    sort: Sort
    """Sorts the ledger account transactions"""

    transaction_at: TransactionAt
    """
    Filters the transactions by date time ranges when the transaction was actually
    performed
    """


_OriginTransactionAtReservedKeywords = TypedDict(
    "_OriginTransactionAtReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class OriginTransactionAt(_OriginTransactionAtReservedKeywords, total=False):
    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End datetime range in UTC"""


class Sort(TypedDict, total=False):
    field: Required[Literal["transaction_at", "origin_transaction_at"]]

    type: Required[Literal["asc", "desc"]]


_TransactionAtReservedKeywords = TypedDict(
    "_TransactionAtReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class TransactionAt(_TransactionAtReservedKeywords, total=False):
    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End datetime range in UTC"""
