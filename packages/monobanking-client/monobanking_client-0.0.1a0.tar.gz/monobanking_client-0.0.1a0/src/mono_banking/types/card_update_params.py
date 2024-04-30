# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    nickname: Optional[str]
    """Card nickname"""

    spending_control_id: Optional[str]
    """Spending control ID"""

    state: Literal["active", "frozen", "canceled", "created"]
    """State of the card"""
