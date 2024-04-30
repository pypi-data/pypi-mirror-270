# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BankListResponse", "PseBanks", "PseBanksBank", "Banks", "BanksBank"]


class PseBanksBank(BaseModel):
    code: Optional[str] = None
    """Returns the PSE bank code."""

    name: Optional[str] = None
    """Returns the PSE bank name."""


class PseBanks(BaseModel):
    banks: Optional[List[PseBanksBank]] = None
    """It contains a list of banks"""

    kind: Optional[str] = None
    """The value of this field will always be `pse`"""


class BanksBank(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    code: Optional[str] = None
    """Returns the bank code."""

    name: Optional[str] = None
    """Returns the bank name."""

    supported_account_types: Optional[List[Literal["savings_account", "checking_account", "electronic_deposit"]]] = None
    """It contains a list of supported account types by a bank"""

    supports_turbo: Optional[bool] = None
    """Informs if bank supports `turbo` transfers"""


class Banks(BaseModel):
    banks: Optional[List[BanksBank]] = None
    """It contains a list of banks"""

    kind: Optional[str] = None
    """The value of this field will always be `transfers`"""


BankListResponse = Union[PseBanks, Banks]
