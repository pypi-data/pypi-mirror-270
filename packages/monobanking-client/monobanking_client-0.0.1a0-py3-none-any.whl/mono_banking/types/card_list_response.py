# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CardListResponse",
    "Card",
    "CardCardholder",
    "CardCardholderAddress",
    "CardCardholderDocument",
    "Pagination",
]


class CardCardholderAddress(BaseModel):
    city: str
    """City, district, suburb, town, or village"""

    country: str
    """Country code ISO 3166-1 alpha-2"""

    line_1: str
    """Street, P.O. Box, or address information"""

    state: str
    """State, province, region, or county"""

    zip_code: str

    extra: Optional[str] = None
    """Additional information"""

    line_2: Optional[str] = None
    """Home, apartment, room, suite, office, or building"""


class CardCardholderDocument(BaseModel):
    number: str
    """Document number"""

    type: Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]
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

    country_code: Optional[str] = None
    """Country code ISO 3166-1 alpha-2"""

    person_type: Optional[Literal["natural", "legal"]] = None
    """The person types can be:

    - legal,
    - natural
    """


class CardCardholder(BaseModel):
    address: CardCardholderAddress
    """Address schema"""

    birthdate: date
    """Cardholder birthdate"""

    document: CardCardholderDocument
    """Person document"""

    email: str
    """Email"""

    first_name: str
    """String field"""

    last_name: str
    """String field"""

    nationality: str
    """Country code ISO 3166-1 alpha-2"""

    phone_number: str
    """Phone number"""

    middle_name: Optional[str] = None
    """String field"""

    second_last_name: Optional[str] = None
    """String field"""


class Card(BaseModel):
    account_id: str
    """Account ID"""

    configuration_group_id: str
    """
    Identifier of the card configuration, you can check it on the endpoint
    /v1/ledger/tenant/config
    """

    id: Optional[str] = None
    """Card ID"""

    cardholder_id: Optional[str] = None
    """Cardholder ID"""

    last_four: Optional[str] = None
    """Last four digits of the card"""

    nickname: Optional[str] = None
    """Card nickname"""

    state: Optional[Literal["active", "frozen", "canceled", "created"]] = None
    """State of the card"""


class Pagination(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Amount of items by page"""

    total_items: Optional[int] = None
    """Total of items by the resource"""

    total_pages: Optional[int] = None
    """Total pages by the resource"""


class CardListResponse(BaseModel):
    cards: Optional[List[Card]] = None
    """Contains a cards list"""

    pagination: Optional[Pagination] = None
    """Pagination schema"""
