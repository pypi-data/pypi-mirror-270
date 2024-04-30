# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountListResponse", "Account", "AccountBalance", "AccountBalanceAvailable", "Pagination"]


class AccountBalanceAvailable(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class AccountBalance(BaseModel):
    available: Optional[AccountBalanceAvailable] = None
    """Money schema"""

    updated_at: Optional[datetime] = None
    """Indicates when the balance was updated"""


class Account(BaseModel):
    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    balance: Optional[AccountBalance] = None
    """Sets balance data"""

    inserted_at: Optional[datetime] = None
    """Indicates when an account balance was created"""

    name: Optional[str] = None
    """
    Represents the name of the account, which is used to describe the account's
    purpose better.
    """

    number: Optional[str] = None
    """Account number"""

    provider: Optional[Literal["coopcentral"]] = None
    """Bank Account provider"""

    state: Optional[Literal["active", "canceled"]] = None
    """
    - active: When the account is active.
    - canceled: When the account was canceled.
    """

    type: Optional[Literal["savings_account"]] = None
    """Account type"""

    updated_at: Optional[datetime] = None
    """Indicates when an account balance was updated"""


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class AccountListResponse(BaseModel):
    accounts: Optional[List[Account]] = None
    """It contains a list with accounts"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""
