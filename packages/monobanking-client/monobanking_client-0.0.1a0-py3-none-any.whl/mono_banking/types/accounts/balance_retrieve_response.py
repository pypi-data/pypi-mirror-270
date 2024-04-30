# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BalanceRetrieveResponse", "Available"]


class Available(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class BalanceRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    available: Optional[Available] = None
    """Money schema"""

    inserted_at: Optional[datetime] = None
    """Indicates when an account balance was created"""

    updated_at: Optional[datetime] = None
    """Indicates when an account balance was updated"""
