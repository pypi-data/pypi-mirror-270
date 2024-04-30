# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BalanceRetrieveResponse", "Available", "Pending"]


class Available(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class Pending(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class BalanceRetrieveResponse(BaseModel):
    available: Optional[Available] = None
    """
    The available balance represents the amount of funds that can be freely used for
    transactions from the account.
    """

    pending: Optional[Pending] = None
    """
    The pending balance represents the amount of funds that are temporarily held or
    reserved in the account, due to pending transactions or authorizations.
    """
