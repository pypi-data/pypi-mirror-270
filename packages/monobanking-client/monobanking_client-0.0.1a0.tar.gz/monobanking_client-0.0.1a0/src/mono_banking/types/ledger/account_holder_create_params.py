# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountHolderCreateParams", "Address", "Person"]


class AccountHolderCreateParams(TypedDict, total=False):
    address: Required[Address]
    """Contains the address information related to the account holder."""

    external_id: Required[Optional[str]]
    """Represents a unique external_id generated and provided by the API user.

    The API user is responsible to generate and provide a unique id for all their
    organization's account holders.
    """

    person: Required[Person]
    """Contains the specific person information of the account holder."""

    email: Optional[str]
    """Account holder's email"""

    metadata: Optional[object]
    """
    Contains additional information that provide context, description, or
    supplementary details about the data being transmitted.
    """

    phone_number: Optional[str]
    """Account holder's phone number"""


class Address(TypedDict, total=False):
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


class Person(TypedDict, total=False):
    country_code: Required[str]
    """
    Country code related to the person, this field use the ISO 3166-1 alpha-2 and
    alpha-3 standards.
    """

    document_number: Required[str]
    """String field"""

    document_type: Required[
        Literal["CC", "TI", "NUIP", "TE", "CE", "NIT", "PASS", "PEP", "PPT", "FDO", "RC", "DL", "NID"]
    ]
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

    first_name: Required[str]

    last_name: Required[str]

    person_type: Required[Literal["natural", "legal"]]
    """Denotes if the person is a natural or a legal entity"""

    middle_name: Optional[str]

    second_last_name: Optional[str]
