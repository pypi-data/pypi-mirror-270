# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BalanceRetrieveParams"]


class BalanceRetrieveParams(TypedDict, total=False):
    live: bool
    """
    if true this will go to the bank and return the `real time` balance otherwise it
    will return the cached balance
    """
