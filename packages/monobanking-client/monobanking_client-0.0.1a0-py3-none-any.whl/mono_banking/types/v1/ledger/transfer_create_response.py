# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TransferCreateResponse", "Amount"]


class Amount(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP", "USD", "MXN"]
    """Currency of money"""


class TransferCreateResponse(BaseModel):
    amount: Amount
    """Money schema"""

    external_id: str
    """Unique identifier of the transfer operation"""

    payer_account_id: str
    """Indicates the format for resource's ID"""

    receiving_account_id: str
    """Indicates the format for resource's ID"""

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    description: Optional[str] = None
    """String field"""

    reference: Optional[str] = None
    """String field"""
