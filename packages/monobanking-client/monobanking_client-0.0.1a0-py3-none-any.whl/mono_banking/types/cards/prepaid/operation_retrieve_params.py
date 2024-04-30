# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OperationRetrieveParams", "PerformedAt"]


class OperationRetrieveParams(TypedDict, total=False):
    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    performed_at: PerformedAt
    """Filters the operations by performed date and time"""


_PerformedAtReservedKeywords = TypedDict(
    "_PerformedAtReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class PerformedAt(_PerformedAtReservedKeywords, total=False):
    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End datetime range in UTC"""
