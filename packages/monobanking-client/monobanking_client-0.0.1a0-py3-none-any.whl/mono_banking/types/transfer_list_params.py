# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferListParams", "InsertedAt", "PayeeDocument", "Sort"]


class TransferListParams(TypedDict, total=False):
    id: str
    """Filters by the transfer ID"""

    account_id: str
    """Filters base on the bank account that money was moved from"""

    batch_id: str
    """Filters transfers by the specific batch were sent"""

    entity_id: str
    """Filters by entity ID"""

    inserted_at: InsertedAt
    """Filters transfers base on creation datetime"""

    page_number: int
    """Number of the page"""

    page_size: int
    """Amount of registers that must be listed by page"""

    payee_account_number: str
    """Filters the transfers by a specific payee's bank account"""

    payee_document: PayeeDocument
    """
    Filters the transfers by a specific payee's national document. Number and type
    must be provided at the same time.
    """

    sort: Sort
    """Sorts transfers depending on the types and fields"""

    state: Literal["created", "in_progress", "cancelled", "declined", "approved", "duplicated"]
    """Filters the transfers by state"""


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


class PayeeDocument(TypedDict, total=False):
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


class Sort(TypedDict, total=False):
    field: Required[Literal["inserted_at", "payee_name"]]

    type: Required[Literal["asc", "desc"]]
