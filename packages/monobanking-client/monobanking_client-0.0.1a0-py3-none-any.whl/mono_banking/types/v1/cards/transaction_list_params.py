# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TransactionListParams", "TransactionAt"]


class TransactionListParams(TypedDict, total=False):
    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    state: Literal["approved", "reversed", "declined"]
    """Filters the transactions by date and time when the transaction was made"""

    transaction_at: TransactionAt
    """Filters the transactions by date and time when the transaction was made"""


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
