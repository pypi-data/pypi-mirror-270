# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypedDict

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    account_id: Union[List[str], str]
    """Filter by one or many account IDs."""

    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    state: Union[
        List[Literal["active", "frozen", "canceled", "created"]], Literal["active", "frozen", "canceled", "created"]
    ]
    """Filter by one or many account IDs."""

    type: Literal["virtual", "plastic"]
    """Filter by one or many account IDs."""
