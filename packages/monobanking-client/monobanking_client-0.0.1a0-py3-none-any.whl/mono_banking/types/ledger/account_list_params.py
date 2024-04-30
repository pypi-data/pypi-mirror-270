# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountListParams", "InsertedAt", "Nickname"]


class AccountListParams(TypedDict, total=False):
    currency_code: List[Literal["COP", "USD", "MXN"]]
    """Filter by the account's currency code"""

    holder: List[str]
    """Filter by account holder ID"""

    inserted_at: InsertedAt
    """Filter accounts based on the range of insertion date and time."""

    nickname: Nickname
    """Filter by account's name"""

    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    state: List[Literal["active", "blocked", "canceled"]]
    """Filter by the account's state"""

    type: List[Literal["subaccount", "current", "bank_settlement", "trade_account", "virtual_settlement"]]
    """Filter by account's type"""


_InsertedAtReservedKeywords = TypedDict(
    "_InsertedAtReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class InsertedAt(_InsertedAtReservedKeywords, total=False):
    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End datetime range in UTC"""


class Nickname(TypedDict, total=False):
    contains: str
    """String field"""

    ends_with: str
    """String field"""

    exact: str
    """String field"""

    not_contains: str
    """String field"""

    starts_with: str
    """String field"""
