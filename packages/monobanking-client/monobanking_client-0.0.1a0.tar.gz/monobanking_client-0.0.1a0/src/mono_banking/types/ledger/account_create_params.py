# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    currency_code: Required[Literal["COP", "USD", "MXN"]]
    """The currency associated with the account balance."""

    holder_id: Required[str]
    """Identifier of the third-party account holder."""

    name: Optional[str]
    """Name of the account, which is used to describe the account's purpose better."""
