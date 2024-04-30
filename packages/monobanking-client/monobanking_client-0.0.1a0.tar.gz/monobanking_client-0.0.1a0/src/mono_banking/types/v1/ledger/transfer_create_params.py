# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransferCreateParams", "Amount"]


class TransferCreateParams(TypedDict, total=False):
    amount: Required[Amount]
    """Money schema"""

    external_id: Required[str]
    """Unique identifier of the transfer operation"""

    payer_account_id: Required[str]
    """Indicates the format for resource's ID"""

    receiving_account_id: Required[str]
    """Indicates the format for resource's ID"""

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
