# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountCreateResponse"]


class AccountCreateResponse(BaseModel):
    currency_code: Literal["COP", "USD", "MXN"]
    """The currency associated with the account balance."""

    holder_id: str
    """Identifier of the third-party account holder."""

    id: Optional[str] = None
    """Indicates the format for resource's ID"""

    inserted_at: Optional[datetime] = None
    """Indicates when a ledger account was created"""

    name: Optional[str] = None
    """Name of the account, which is used to describe the account's purpose better."""

    provider: Optional[Literal["mono_ledger"]] = None
    """
    Specifies the provider of the account, for ledger accounts, the provider will be
    always `mono_ledger`
    """

    state: Optional[Literal["active", "blocked", "canceled"]] = None
    """State of the account, it can be one of the following values:

    - active: it's enabled to perform operations with the account balance.
    - blocked: it's disabled by a tenant and couldn't perform any operation with the
      account balance.
    - canceled: it's disabled by Mono and couldn't perform any operation with the
      account balance.
    """

    state_reason: Optional[Literal["temporary", "user_request", "unused", "fraud", "other"]] = None
    """It provides the reason why the account could be blocked or canceled.

    It is required when the account is transitioned to being blocked or canceled.
    """

    state_reason_detail: Optional[str] = None
    """
    It provides a textual reason why the account is blocked in case of the
    state_reason value is `other`.
    """

    type: Optional[Literal["subaccount", "current"]] = None
    """Type of the account, it can be one of the following values:

    - subaccount: Account that belongs to a third-party account holder, you can
      create an unlimited number of accounts for any third-party account holder.
    - current: This is an special account that provides a clear overview of the
      available funds for a tenant. It serves as a read-only account, showcasing the
      current financial standing without the capability to create new ledger
      accounts.
    """

    updated_at: Optional[datetime] = None
    """Indicates when a ledger account was updated"""
