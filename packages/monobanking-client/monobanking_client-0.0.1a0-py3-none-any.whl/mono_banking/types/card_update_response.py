# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardUpdateResponse", "Cardholder", "CardholderAddress", "CardholderDocument", "InitialBalance"]


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


class InitialBalance(BaseModel):
    amount: int
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Literal["COP"]
    """Currency of money"""


class CardUpdateResponse(BaseModel):
    account_id: str
    """Account ID"""

    id: Optional[str] = None
    """Card ID"""

    cardholder_id: Optional[str] = None
    """Cardholder ID"""

    configuration_group_id: Optional[str] = None
    """Card configuration group ID.

    By default, if the configuration group ID is not specified, it is taken from the
    client's default configuration.
    """

    last_four: Optional[str] = None
    """Last four digits of the card"""

    nickname: Optional[str] = None
    """Card nickname"""

    state: Optional[Literal["active", "frozen", "canceled", "created"]] = None
    """State of the card"""
