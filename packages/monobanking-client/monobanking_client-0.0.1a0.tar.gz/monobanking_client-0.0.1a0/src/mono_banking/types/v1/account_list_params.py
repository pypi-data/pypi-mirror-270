# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""
