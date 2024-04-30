# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IntentListParams"]


class IntentListParams(TypedDict, total=False):
    page_number: int
    """Page number"""

    page_size: int
    """Page size"""

    state: Literal["all", "created", "in_progress", "approved_in_provider", "account_credited", "failed"]
    """State of the collection intents"""
