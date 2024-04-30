# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BalanceTopupOrWithdrawParams", "Amount"]


class BalanceTopupOrWithdrawParams(TypedDict, total=False):
    amount: Required[Amount]
    """Money schema"""

    external_id: Required[str]
    """Unique identifier of the update balance operation"""

    operation: Required[Literal["topup", "withdrawal"]]
    """
    Operation type to perform an update balance, it can be one of the following
    options:

    - `topup`: Increment the account balance.
    - `withdrawal`: Decrease the account balance.
    """

    description: Optional[str]
    """String field"""

    reference: Optional[str]
    """String field"""


class Amount(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP", "USD", "MXN"]]
    """Currency of money"""
