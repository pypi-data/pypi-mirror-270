# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CardCreateResponse", "Cardholder", "CardholderAddress", "CardholderDocument"]


class CardholderAddress(BaseModel):
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


class CardholderDocument(BaseModel):
    country_code: str
    """Country code ISO 3166-1 alpha-2"""

    number: str
    """Document number"""

    person_type: Literal["natural", "legal"]
    """The person types can be:

    - legal,
    - natural
    """

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


class Cardholder(BaseModel):
    address: CardholderAddress
    """Address schema"""

    birthdate: date
    """Cardholder birthdate"""

    document: CardholderDocument
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


class CardCreateResponse(BaseModel):
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
