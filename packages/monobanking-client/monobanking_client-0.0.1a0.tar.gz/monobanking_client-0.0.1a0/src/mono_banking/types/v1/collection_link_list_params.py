# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CollectionLinkListParams", "ExpiresAt", "InsertedAt", "Payer", "PayerDocument", "Sort"]


class CollectionLinkListParams(TypedDict, total=False):
    enabled: bool
    """Filter by enabled field"""

    expires_at: ExpiresAt
    """Filter by expires_at field, it works as with range of date/time."""

    external_id: str
    """Filter by external id field"""

    inserted_at: InsertedAt
    """Filter by a range of date/time"""

    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    payer: Payer
    """Filter by payer info"""

    reference: str
    """
    Filter by reference field, it works as not exact filter and must be sent 4
    characters at least.
    """

    sort: Sort
    """Sorts the collection links according to the types and fields."""


_ExpiresAtReservedKeywords = TypedDict(
    "_ExpiresAtReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class ExpiresAt(_ExpiresAtReservedKeywords, total=False):
    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End datetime range in UTC"""


_InsertedAtReservedKeywords = TypedDict(
    "_InsertedAtReservedKeywords",
    {
        "from": Union[str, datetime],
    },
    total=False,
)


class InsertedAt(_InsertedAtReservedKeywords, total=False):
    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End datetime range in UTC"""


class PayerDocument(TypedDict, total=False):
    number: Required[str]
    """Document number"""

    type: Required[Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]]
    """The document types are represented by codes and can be:

    For Colombia:

    - CC
    - TI
    - NUIP
    - TE
    - CE
    - NIT
    - PASS
    - PEP
    - PPT
    - FDO
    - RC

    For other countries:

    - NID (National Identification)
    - DL (Driver License)
    - PASS
    """

    country_code: str
    """Country code ISO 3166-1 alpha-2"""

    person_type: Literal["natural", "legal"]
    """The person types can be:

    - legal,
    - natural
    """


class Payer(TypedDict, total=False):
    document: PayerDocument
    """Filter by document"""

    name: str
    """Filter by payer name"""


class Sort(TypedDict, total=False):
    field: Required[Literal["inserted_at"]]

    type: Required[Literal["asc", "desc"]]
