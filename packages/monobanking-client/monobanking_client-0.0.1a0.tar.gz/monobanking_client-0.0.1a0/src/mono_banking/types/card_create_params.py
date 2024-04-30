# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardCreateParams", "Cardholder", "CardholderAddress", "CardholderDocument", "InitialBalance"]


class CardCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    cardholder: Required[Cardholder]
    """Represents the cardholder information"""

    configuration_group_id: Optional[str]
    """Card configuration group ID.

    By default, if the configuration group ID is not specified, it is taken from the
    client's default configuration.
    """

    initial_balance: Optional[InitialBalance]
    """The current amount available or the balance"""

    nickname: Optional[str]
    """Card nickname"""


class CardholderAddress(TypedDict, total=False):
    city: Required[str]
    """City, district, suburb, town, or village"""

    country: Required[str]
    """Country code ISO 3166-1 alpha-2"""

    line_1: Required[str]
    """Street, P.O. Box, or address information"""

    state: Required[str]
    """State, province, region, or county"""

    zip_code: Required[str]

    extra: Optional[str]
    """Additional information"""

    line_2: Optional[str]
    """Home, apartment, room, suite, office, or building"""


class CardholderDocument(TypedDict, total=False):
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


class Cardholder(TypedDict, total=False):
    address: Required[CardholderAddress]
    """Address schema"""

    birthdate: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Cardholder birthdate"""

    document: Required[CardholderDocument]
    """Person document"""

    email: Required[str]
    """Email"""

    first_name: Required[str]
    """String field"""

    last_name: Required[str]
    """String field"""

    nationality: Required[str]
    """Country code ISO 3166-1 alpha-2"""

    phone_number: Required[str]
    """Phone number"""

    middle_name: Optional[str]
    """String field"""

    second_last_name: Optional[str]
    """String field"""


class InitialBalance(TypedDict, total=False):
    amount: Required[int]
    """Amount of money in `cents` with the format is int64.

    Thus, you send an integer "10.000.000", we will interpret it as "100.000,00"
    """

    currency: Required[Literal["COP"]]
    """Currency of money"""
