# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SpendingControlListParams"]


class SpendingControlListParams(TypedDict, total=False):
    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    target: Literal["card"]
    """Target of the spending control"""
