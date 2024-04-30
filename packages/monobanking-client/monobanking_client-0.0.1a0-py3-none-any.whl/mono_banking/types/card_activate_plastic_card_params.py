# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CardActivatePlasticCardParams"]


class CardActivatePlasticCardParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    cardholder_id: Required[str]
    """Cardholder ID"""

    configuration_group_id: Required[str]
    """Card Config Group ID"""

    spending_control_id: Optional[str]
    """Spending Control ID"""
