# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationCreateParams", "Amount"]


class OperationCreateParams(TypedDict, total=False):
    amount: Required[Amount]
    """deposit balance amount"""

    operation: Required[Literal["topup", "withdrawal"]]
    """there are two operation types:

    - topup: Increments the card balance.
    - withdrawal: Reduces the card balance.
    """

    description: Optional[str]
    """String field"""

    entity_id: str
    """String field"""


class Amount(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP"]]
    """Currency of money"""
