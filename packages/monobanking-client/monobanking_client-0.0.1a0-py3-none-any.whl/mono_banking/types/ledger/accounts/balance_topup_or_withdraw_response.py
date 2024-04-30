# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BalanceTopupOrWithdrawResponse", "Amount"]


class Amount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class BalanceTopupOrWithdrawResponse(BaseModel):
    amount: Amount
    """Money schema"""

    external_id: str
    """Unique identifier of the update balance operation"""

    operation: Literal["topup", "withdrawal"]
    """
    Operation type to perform an update balance, it can be one of the following
    options:

    - `topup`: Increment the account balance.
    - `withdrawal`: Decrease the account balance.
    """

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    description: Optional[str] = None
    """String field"""

    reference: Optional[str] = None
    """String field"""
