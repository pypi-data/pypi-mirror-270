# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BalanceRetrieveResponse", "Balance"]


class Balance(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class BalanceRetrieveResponse(BaseModel):
    balance: Optional[Balance] = None
    """Amount available on the card"""

    card_id: Optional[str] = None
    """Card ID"""
